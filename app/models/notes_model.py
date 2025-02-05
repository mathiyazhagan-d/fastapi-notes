from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Note(BaseModel):
    note_id: Optional[str] = None
    note_title: str
    note_content: str
    user_id: str
    created_on: datetime = Field(default_factory=datetime.utcnow)
    last_update: datetime = Field(default_factory=datetime.utcnow)
