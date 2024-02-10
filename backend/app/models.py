from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4

class User(SQLModel, table=True):
    """
    Represents a user with a unique identifier, tasks, time blocks, and time logs.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(sa_column_kwargs={"unique": True})

class Category(SQLModel, table=True):
    """
    Represents a category for tasks and time blocks, unique to a user.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")
    name: str
    description: Optional[str] = None
    user: User = Relationship(back_populates="categories")

class Task(SQLModel, table=True):
    """
    Represents a task, associated with a user-specific category.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")
    title: str
    description: Optional[str] = None
    category_id: UUID = Field(foreign_key="category.id")
    due_date: Optional[datetime] = None
    completed: bool = False
    category: Category = Relationship(back_populates="tasks")

class TimeBlock(SQLModel, table=True):
    """
    Represents a planned block of time for a particular activity, associated with a user-specific category.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")
    start_time: datetime
    end_time: datetime
    category_id: UUID = Field(foreign_key="category.id")
    description: Optional[str] = None
    category: Category = Relationship(back_populates="time_blocks")

class TimeLog(SQLModel, table=True):
    """
    Represents an actual log of time spent on activities, associated with a user-specific category.
    """
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")
    start_time: datetime
    end_time: datetime
    category_id: UUID = Field(foreign_key="category.id")
    description: Optional[str] = None
    category: Category = Relationship(back_populates="time_logs")

# Establish relationships
User.categories: List[Category] = Relationship(back_populates="user")
Category.tasks: List[Task] = Relationship(back_populates="category")
Category.time_blocks: List[TimeBlock] = Relationship(back_populates="category")
Category.time_logs: List[TimeLog] = Relationship(back_populates="category")

        