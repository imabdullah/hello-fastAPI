from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI()

# Database setup
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER") 
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# User model
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    username = Column(String(100))
    full_name = Column(String(255))
    is_active = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

@app.get("/")
def home():
    return {"message": "FastAPI is working!"}

@app.get("/users")
def get_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        result = []
        for user in users:
            result.append({
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "full_name": user.full_name,
                "is_active": user.is_active,
                "created_at": str(user.created_at),
                "updated_at": str(user.updated_at)
            })
        return {"users": result}
    finally:
        db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)