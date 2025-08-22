from fastapi import APIRouter, Depends

from app.dependencies import get_user_service
from app.schemas.user import UserListResponse, UserResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_all_users(skip: int = 0, limit: int = 100, user_service: UserService = Depends(get_user_service)):
    result = user_service.get_all_users(skip=skip, limit=limit)
    return UserListResponse(
        users = [UserResponse.from_orm(u) for u in result["users"]],
        total = result["total"],
        page=result["page"],
    )