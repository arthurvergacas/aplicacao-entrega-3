import dotenv
import os

dotenv.load_dotenv()


def get_env_variable(key: str) -> str:
    variable = os.getenv(key)

    if variable is None:
        raise ValueError(
            f"Environment variable '{key}' does not exist. Make sure you have a '.env' file in the root of your project."
        )

    return variable
