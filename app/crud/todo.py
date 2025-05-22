from sqlalchemy.orm import Session
from app.models.todo import Todo 
from app.schemas.todo import TodoCreate,TodoUpdate
import uuid

def get_todo(db:Session,todo_id:uuid.UUID):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def get_todos(db:Session,skip: int = 0,limit: int = 100 ):
    return db.query(Todo).offset(skip).limit(limit).all()

def create_todo(db:Session,todo:TodoCreate):
    add_todo = Todo(
        title = todo.title,
        description = todo.description,
        completed = todo.completed
    )
    db.add(add_todo)
    db.commit()
    db.refresh(add_todo)
    return add_todo

def update_todo(db:Session,todo_id:uuid.UUID,todo:TodoUpdate):
    up_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if up_todo is None:
        return None 
    if todo.title is not None:
        up_todo.title = todo.title 
    if todo.description is not None:
        up_todo.description = todo.description
    if todo.completed is not None:
        up_todo.completed = todo.completed 
    
    db.commit()
    db.refresh(up_todo)
    return up_todo 

def delete_todo(db:Session,todo_id:uuid.UUID):
    del_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if del_todo is None:
        return None 
    
    db.delete(del_todo)
    db.commit()
    return del_todo 

