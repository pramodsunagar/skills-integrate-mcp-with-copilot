"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Import auth router and role helpers
from src.auth import router as auth_router, require_role
app.include_router(auth_router, prefix="/auth")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# Replace in-memory store with persistent DB
from src.db import create_db_and_tables, get_session, Activity as DBActivity, Participant as DBParticipant
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

# Create DB and seed if necessary
create_db_and_tables()


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities(session=Depends(get_session)):
    stmt = select(DBActivity)
    results = session.exec(stmt).all()
    out = {}
    for a in results:
        parts = session.exec(select(DBParticipant).where(DBParticipant.activity_id == a.id)).all()
        out[a.name] = {
            "description": a.description,
            "schedule": a.schedule,
            "max_participants": a.max_participants,
            "participants": [p.email for p in parts]
        }
    return out


from pydantic import BaseModel


class ActivityCreate(BaseModel):
    name: str
    description: str
    schedule: str
    max_participants: int


@app.post("/activities", status_code=status.HTTP_201_CREATED)
def create_activity(activity: ActivityCreate, _=Depends(require_role(["organizer", "admin"])), session=Depends(get_session)):
    """Create a new activity (protected: organizer/admin)"""
    db_act = DBActivity(name=activity.name, description=activity.description, schedule=activity.schedule, max_participants=activity.max_participants)
    try:
        session.add(db_act)
        session.commit()
        session.refresh(db_act)
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=409, detail="Activity already exists")
    return {"message": f"Created activity {db_act.name}"}


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str, session=Depends(get_session)):
    """Sign up a student for an activity"""
    stmt = select(DBActivity).where(DBActivity.name == activity_name)
    act = session.exec(stmt).first()
    if not act:
        raise HTTPException(status_code=404, detail="Activity not found")
    parts = session.exec(select(DBParticipant).where(DBParticipant.activity_id == act.id)).all()
    if any(p.email == email for p in parts):
        raise HTTPException(status_code=400, detail="Student is already signed up")
    if len(parts) >= act.max_participants:
        raise HTTPException(status_code=400, detail="Activity is full")
    p = DBParticipant(email=email, activity_id=act.id)
    session.add(p)
    session.commit()
    return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str, session=Depends(get_session)):
    """Unregister a student from an activity"""
    stmt = select(DBActivity).where(DBActivity.name == activity_name)
    act = session.exec(stmt).first()
    if not act:
        raise HTTPException(status_code=404, detail="Activity not found")
    participant = session.exec(select(DBParticipant).where((DBParticipant.activity_id == act.id) & (DBParticipant.email == email))).first()
    if not participant:
        raise HTTPException(status_code=400, detail="Student is not signed up for this activity")
    session.delete(participant)
    session.commit()
    return {"message": f"Unregistered {email} from {activity_name}"}
