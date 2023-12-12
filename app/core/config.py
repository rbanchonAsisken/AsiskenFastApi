import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # DB_CONNECTOR: str = '//172.18.42.9:5690/asisken/api/db'
    DB_CONNECTOR: str = 'http://localhost:5690/api/db'
    DB_CONNECTOR_SQL: str = 'http://localhost:5960/api/db'
    DEBUG: bool = False


settings = Settings()
