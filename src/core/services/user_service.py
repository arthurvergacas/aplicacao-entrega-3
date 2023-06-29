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
        connection = DBConnection()
        user_dict: dict = vars(user)
        insert = """
        INSERT INTO USUARIO 
        VALUES (:email, :cpf, :name, TO_DATE(:birth_date, 'DD/MM/YYYY'), 
        :sexuality, :gender, :blindness_degree, :description, :audio_url, 
        :img_url)
        """
        connection.execute(insert, user_dict)
