from typing import Optional

from models.user import User
from core.infra.connection import DBConnection


class UserService:
    @staticmethod
    def search_users(name: str) -> list[User]:
        connection = DBConnection()
        select = """
        SELECT *
        FROM USUARIO U
        WHERE LOWER(U.nome) LIKE :name
        """

        cursor = connection.execute(select, {"name": f"%{name.lower().strip()}%"})

        if cursor is None:
            return []

        return [User(*row) for row in cursor.fetchall()]

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
