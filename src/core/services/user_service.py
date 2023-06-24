from typing import Optional

from models.user import User
from core.infra.connection import DBConnection


class UserService:
    @staticmethod
    def search_users(name: Optional[str] = None) -> list[User]:
        connection = DBConnection()
        return []

    @staticmethod
    def create_user(user: User) -> None:
        pass
