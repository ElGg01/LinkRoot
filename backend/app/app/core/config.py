import os

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    APP_LICENSE_NAME: str = "MIT"
    APP_LICENSE_URL: str = "https://opensource.org/licenses/MIT"
    CORS_ORIGINS: list[str] = ["http://127.0.0.1:3000", "http://localhost:3000"]
    MIDDLEWARE_ALLOW_CREDENTIALS: bool = True
    MIDDLEWARE_ALLOW_METHODS: list[str] = ["*"]
    MIDDLEWARE_ALLOW_HEADERS: list[str] = ["*"]
    API_V1_STR: str = "/api/v1"

    # DB
    DB_URI: str = os.getenv("DB_URI", "")


settings = Settings()
