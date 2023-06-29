from __future__ import annotations
from typing import Any, Optional, Type
import oracledb
from utils.env_variables import get_env_variable


class DBConnection:
    connection: oracledb.Connection | None = None

    def __init__(
        self,
        db_data_source: Optional[str] = None,
        db_user: Optional[str] = None,
        db_password: Optional[str] = None,
    ) -> None:
        if DBConnection.connection is None:
            if (
                db_data_source is not None
                and db_user is not None
                and db_password is not None
            ):
                DBConnection.connection = self.__create_connection(
                    db_data_source, db_user, db_password
                )
            else:
                raise Exception(
                    "Database connection not created. Use DBConnection.create() before instantiating a new DBConnection"
                )

    def execute(
        self, statement: str, parameters: Optional[dict[Any, Any]] = None
    ) -> oracledb.Cursor | None:
        if DBConnection.connection is None:
            raise Exception(
                "You must instantiate DBConnection before executing SQL statements"
            )
        result_cursor: oracledb.Cursor | None = DBConnection.connection.cursor().execute(statement, parameters)  # type: ignore # 😠
        DBConnection.connection.commit()

        if result_cursor is not None:
            return result_cursor
        
    def __create_connection(
        self, db_data_source: str, db_user: str, db_password: str
    ) -> oracledb.Connection:
        connection: oracledb.Connection = oracledb.connect(
            user=db_user, password=db_password, dsn=db_data_source
        )

        return connection

    @classmethod
    def create(cls: Type[DBConnection]) -> DBConnection:
        return DBConnection(
            get_env_variable("DB_DATA_SOURCE"),
            get_env_variable("DB_USER"),
            get_env_variable("DB_PASSWORD"),
        )
    
