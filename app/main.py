from fastapi import FastAPI
from dotenv import load_dotenv
import os

from app.api.v1.endpoints import todos
from app.database.base import Base, engine

load_dotenv()

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo API",
    description="A simple Todo API with FastAPI and Supabase",
    version="0.1.0",
)

app.include_router(
    todos.router,
    prefix="/api/v1/todos",
    tags=["todos"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}