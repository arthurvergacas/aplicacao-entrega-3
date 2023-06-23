import oracledb


class DBConnection:
    connection: oracledb.Connection | None = None

    def __init__(self, db_data_source: str, db_user: str, db_password: str) -> None:
        if DBConnection.connection is None:
            DBConnection.connection = self.__create_connection(
                db_data_source, db_user, db_password
            )

    def __create_connection(
        self, db_data_source: str, db_user: str, db_password: str
    ) -> oracledb.Connection:
        connection: oracledb.Connection = oracledb.connect(
            user=db_user, password=db_password, dsn=db_data_source
        )

        print("Successfully connected to Oracle Database")

        return connection
