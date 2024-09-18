from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = "sqlite://../database.db"
    MODULES: dict = {"models": ["src.models"]}


settings = Settings()
