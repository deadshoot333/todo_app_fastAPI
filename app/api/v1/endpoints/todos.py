from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uuid

from app.schemas.todo import Todo, TodoCreate, TodoUpdate
from app.crud.todo import (
    get_todo, get_todos, create_todo, update_todo, delete_todo
)
from app.database.base import get_db

router = APIRouter()

@router.post("/", response_model=Todo)
def create_todo_endpoint(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db=db, todo=todo)

@router.get("/", response_model=List[Todo])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = get_todos(db, skip=skip, limit=limit)
    return todos

@router.get("/{todo_id}", response_model=Todo)
def read_todo(todo_id: uuid.UUID, db: Session = Depends(get_db)):
    db_todo = get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.put("/{todo_id}", response_model=Todo)
def update_todo_endpoint(
    todo_id: uuid.UUID, todo: TodoUpdate, db: Session = Depends(get_db)
):
    db_todo = update_todo(db, todo_id=todo_id, todo=todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.delete("/{todo_id}", response_model=Todo)
def delete_todo_endpoint(todo_id: uuid.UUID, db: Session = Depends(get_db)):
    db_todo = delete_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo