from typing import Optional

from models.user import User


class UserService:
    @staticmethod
    def search_users(name: Optional[str] = None) -> list[User]:
        return []

    @staticmethod
    def create_user(user: User) -> None:
        pass
