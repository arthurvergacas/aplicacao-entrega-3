from typing import Any, Optional
import oracledb


class DBConnection:
    connection: oracledb.Connection | None = None

    def __init__(self, db_data_source: str, db_user: str, db_password: str) -> None:
        if DBConnection.connection is None:
            DBConnection.connection = self.__create_connection(
                db_data_source, db_user, db_password
            )

    def execute(
        self, statement: str, parameters: Optional[dict[Any, Any]] = None
    ) -> oracledb.Cursor | None:
        if DBConnection.connection is None:
            raise Exception(
                "You must instantiate DBConnection before executing SQL statements"
            )

        result_cursor: oracledb.Cursor | None =
                DBConnection.connection.cursor().execute(statement, parameters)  # type: ignore # 😠

        if result_cursor is not None:
            return result_cursor

    def __create_connection(
        self, db_data_source: str, db_user: str, db_password: str
    ) -> oracledb.Connection:
        connection: oracledb.Connection = oracledb.connect(
            user=db_user, password=db_password, dsn=db_data_source
        )

        print("Successfully connected to Oracle Database")

        return connection
