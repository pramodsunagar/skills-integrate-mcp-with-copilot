from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship, create_engine, Session, select

DATABASE_URL = "sqlite:///./activities.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


class Participant(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    activity_id: Optional[int] = Field(default=None, foreign_key="activity.id")
    activity: "Activity" = Relationship(back_populates="participants")


class Activity(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    schedule: str
    max_participants: int
    participants: List[Participant] = Relationship(back_populates="activity")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    # seed initial data if empty
    with Session(engine) as session:
        stmt = select(Activity)
        first = session.exec(stmt).first()
        if not first:
            seed = [
                Activity(name="Chess Club", description="Learn strategies and compete in chess tournaments", schedule="Fridays, 3:30 PM - 5:00 PM", max_participants=12),
                Activity(name="Programming Class", description="Learn programming fundamentals and build software projects", schedule="Tuesdays and Thursdays, 3:30 PM - 4:30 PM", max_participants=20),
                Activity(name="Gym Class", description="Physical education and sports activities", schedule="Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM", max_participants=30),
            ]
            session.add_all(seed)
            session.commit()


def get_session():
    with Session(engine) as session:
        yield session
