from pydantic import BaseModel, EmailStr
from datetime import datetime
import uuid

class User(BaseModel):
    user_id: str = str(uuid.uuid4())
    user_name: str
    user_email: EmailStr
    password: str
    created_on: datetime = datetime.utcnow()
    last_update: datetime = datetime.utcnow()

class UserLogin(BaseModel):
    user_email: EmailStr
    password: str

class UserRegister(BaseModel):
    user_name: str
    user_email: EmailStr
    password: str
