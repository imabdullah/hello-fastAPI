from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self, skip: int = 0, limit: int = 100):  # Add self here
        users = self.user_repository.get_all_users(skip=skip, limit=limit)
        total_count = self.user_repository.count_active_users()
        return {
            "users": users,
            "total": total_count,
            "page": skip // limit + 1 if limit > 0 else 1
        }