from pydantic import BaseModel,UUID4
from typing import Optional 
import uuid 

class TodoBase(BaseModel):
    title : str 
    description : Optional[str] = None 
    completed : bool = False

class TodoCreate(TodoBase):
    pass 

class TodoUpdate(TodoBase):
    title : Optional[str] = None 
    description : Optional[str] = None 
    completed : Optional[bool] = None 
    
class Todo(TodoBase):
    id: UUID4 
    
    class Config:
        orm_mode = True 