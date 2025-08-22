from app.models.user import User


class UserRepository:

    def __init__(self, db):
        self.db = db

    def get_all_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(User).offset(skip).limit(limit).all()

    def count_active_users(self):
        return self.db.query(User).filter(User.is_active == True).count()