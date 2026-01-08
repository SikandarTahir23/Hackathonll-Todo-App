from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
import uuid

from .todo_model import Todo


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(nullable=False, max_length=255)
    email: str = Field(nullable=False, unique=True, max_length=255)
    password_hash: str = Field(nullable=False, max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)

    # Relationship to Todos
    todos: List[Todo] = Relationship(back_populates="user", cascade_delete=True)