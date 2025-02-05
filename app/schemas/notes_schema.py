from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional
import uuid

class Note(BaseModel):
    note_id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    note_title: str
    note_content: str
    user_id: str
    created_on: datetime = Field(default_factory=datetime.utcnow)
    last_update: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
