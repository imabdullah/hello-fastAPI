from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def get_user_service(user_repo: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(user_repo)
