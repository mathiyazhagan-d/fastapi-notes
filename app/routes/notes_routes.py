from fastapi import APIRouter, Depends, HTTPException
from app.services.notes_controller import (
    create_note,
    get_notes,
    get_note_by_id,
    update_note,
    delete_note,
)
from app.models.note_schema import Note
from typing import List
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/notes", tags=["Notes"])

# Create Note
@router.post("/", response_model=dict)
async def create_note_endpoint(note: Note, current_user: dict = Depends(get_current_user)):
    note.user_id = current_user["user_id"]
    return await create_note(note)

# Get All Notes for Logged-in User
@router.get("/", response_model=List[dict])
async def get_notes_endpoint(current_user: dict = Depends(get_current_user)):
    return await get_notes(current_user["user_id"])

# Get Note by ID
@router.get("/{note_id}", response_model=dict)
async def get_note_by_id_endpoint(note_id: str):
    return await get_note_by_id(note_id)

# Update Note
@router.put("/{note_id}", response_model=dict)
async def update_note_endpoint(note_id: str, note: Note, current_user: dict = Depends(get_current_user)):
    return await update_note(note_id, note)

# Delete Note
@router.delete("/{note_id}", response_model=dict)
async def delete_note_endpoint(note_id: str, current_user: dict = Depends(get_current_user)):
    return await delete_note(note_id)
