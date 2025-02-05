from app.database import notes_collection
from app.models.note_schema import Note
from bson import ObjectId
from datetime import datetime
from fastapi import HTTPException

# Create a new note
async def create_note(note_data: Note):
    note_dict = note_data.dict()
    note_dict["_id"] = str(ObjectId())  # Generate MongoDB ObjectId
    await notes_collection.insert_one(note_dict)
    return {"message": "Note created successfully", "note": note_dict}

# Get all notes for a user
async def get_notes(user_id: str):
    notes = await notes_collection.find({"user_id": user_id}).to_list(100)
    return [
        {
            "note_id": str(note["_id"]),
            "note_title": note["note_title"],
            "note_content": note["note_content"],
            "user_id": note["user_id"],
            "created_on": note["created_on"],
            "last_update": note["last_update"],
        }
        for note in notes
    ]

# Get a single note by ID
async def get_note_by_id(note_id: str):
    note = await notes_collection.find_one({"_id": note_id})
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {
        "note_id": str(note["_id"]),
        "note_title": note["note_title"],
        "note_content": note["note_content"],
        "user_id": note["user_id"],
        "created_on": note["created_on"],
        "last_update": note["last_update"],
    }

# Update a note
async def update_note(note_id: str, note_data: Note):
    note_data.last_update = datetime.utcnow()
    updated_note = await notes_collection.update_one(
        {"_id": note_id}, {"$set": note_data.dict(exclude_unset=True)}
    )
    if updated_note.modified_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note updated successfully"}

# Delete a note
async def delete_note(note_id: str):
    deleted_note = await notes_collection.delete_one({"_id": note_id})
    if deleted_note.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted successfully"}
