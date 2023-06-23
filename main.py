from utils.env_variables import get_env_variable
from core.connection import DBConnection


def run() -> None:
    connection = DBConnection(
        get_env_variable("DB_DATA_SOURCE"),
        get_env_variable("DB_USER"),
        get_env_variable("DB_PASSWORD"),
    )


if __name__ == "__main__":
    run()
