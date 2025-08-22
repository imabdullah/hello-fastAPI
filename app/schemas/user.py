from datetime import datetime
from typing import List

from pydantic import BaseModel


class UserResponse(BaseModel):
    email: str
    username: str
    full_name: str | None = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserListResponse(BaseModel):
    users: List[UserResponse]
    total: int
    page: int