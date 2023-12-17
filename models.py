# this file will have the data classes

from typing import Optional
from sqlmodel import Field, SQLModel, create_engine


class ExampleHero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


class Meditation(SQLModel, table=True):
    timestamp: int
    duration: int


class Poop(SQLModel, table=True):
    timestamp: int
    type: Optional[int] = None


class Exercise(SQLModel, table=True):
    timestamp: int
    duration: int
    type: str
    


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)