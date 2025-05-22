from sqlalchemy import Boolean,Column,ForeignKey,Integer,String
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy.orm import relationship
from ..database.base import Base 
import uuid

class Todo(Base):
    __tablename__ = "todos"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4,unique=True,nullable=False)
    title = Column(String,index=True)
    description = Column(String,index=True)
    completed = Column(Boolean,default=False)
    
    def __repr__(self):
        return f"<Todo object created id={self.id} title={self.title}>"