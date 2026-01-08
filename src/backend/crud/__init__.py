from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from typing import List
from .models.user_model import User
from .models.todo_model import Todo
from .schemas.auth import UserCreate
from .schemas.todo import TodoCreate, TodoUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.password_hash):
        return None
    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = get_password_hash(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        password_hash=fake_hashed_password
    )
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise ValueError("User with this email already exists")


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()


def get_todos_by_user(db: Session, user_id: str, skip: int = 0, limit: int = 100):
    return db.query(Todo).filter(Todo.user_id == user_id).offset(skip).limit(limit).all()


def get_todo(db: Session, todo_id: str):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def create_todo(db: Session, todo: TodoCreate, user_id: str):
    db_todo = Todo(**todo.dict(), user_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, todo_id: str, todo: TodoUpdate):
    db_todo = get_todo(db, todo_id)
    if db_todo is None:
        return None
    
    update_data = todo.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)
    
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: str):
    db_todo = get_todo(db, todo_id)
    if db_todo is None:
        return False
    
    db.delete(db_todo)
    db.commit()
    return True