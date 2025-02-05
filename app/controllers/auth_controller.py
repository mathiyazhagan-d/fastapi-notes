from app.database import db
from app.utils.hashing import hash_password, verify_password
from app.utils.jwt_handler import create_jwt
from fastapi import HTTPException

async def register_user(data: UserRegister):
    existing_user = await db.users.find_one({"user_email": data.user_email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_password = hash_password(data.password)
    new_user = User(
        user_id=str(uuid.uuid4()),
        user_name=data.user_name,
        user_email=data.user_email,
        password=hashed_password,
        created_on=datetime.utcnow(),
        last_update=datetime.utcnow()
    )
    await db.users.insert_one(new_user.dict())
    return {"message": "User registered successfully"}

async def login_user(data: UserLogin):
    user = await db.users.find_one({"user_email": data.user_email})
    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = create_jwt({"user_id": user["user_id"], "user_email": user["user_email"]})
    return {"access_token": token}