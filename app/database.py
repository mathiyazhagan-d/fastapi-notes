from pymongo import MongoClient
from app.config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["notes-py"]  # Change "notes_app" to your preferred database name
