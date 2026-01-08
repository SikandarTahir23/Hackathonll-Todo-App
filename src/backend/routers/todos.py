from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .database import get_session
from .models.todo_model import Todo
from .schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from . import crud
from better_auth.api.fastapi import get_current_user
from uuid import UUID

router = APIRouter()


@router.get("/", response_model=List[TodoResponse])
def get_todos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    # Only return todos for the current user
    todos = crud.get_todos_by_user(db, user_id=current_user.id, skip=skip, limit=limit)
    return todos


@router.post("/", response_model=TodoResponse)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    return crud.create_todo(db=db, todo=todo, user_id=current_user.id)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(
    todo_id: str,
    db: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_todo = crud.get_todo(db, todo_id=todo_id)
    if db_todo is None or str(db_todo.user_id) != str(current_user.id):
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: str,
    todo: TodoUpdate,
    db: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_todo = crud.get_todo(db, todo_id=todo_id)
    if db_todo is None or str(db_todo.user_id) != str(current_user.id):
        raise HTTPException(status_code=404, detail="Todo not found")

    updated_todo = crud.update_todo(db, todo_id=todo_id, todo=todo)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo


@router.delete("/{todo_id}")
def delete_todo(
    todo_id: str,
    db: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    db_todo = crud.get_todo(db, todo_id=todo_id)
    if db_todo is None or str(db_todo.user_id) != str(current_user.id):
        raise HTTPException(status_code=404, detail="Todo not found")

    success = crud.delete_todo(db, todo_id=todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}