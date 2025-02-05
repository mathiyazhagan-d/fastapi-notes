from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow frontend requests (Replace with your frontend URL in production)
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy users
users = {"admin@example.com": "password"}

# In-memory Notes Storage
notes = []

class Note(BaseModel):
    id: int
    title: str
    content: str

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(data: LoginRequest):
    if data.email in users and users[data.email] == data.password:
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/notes", response_model=List[Note])
def get_notes():
    return notes

@app.post("/notes")
def add_note(note: Note):
    notes.append(note)
    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    global notes
    notes = [note for note in notes if note.id != note_id]
    return {"message": "Note deleted"}
