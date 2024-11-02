from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./database.sqlite3"
    SECRET_KEY = '7oHQyjS2lQIcK7k1pfyWE0KnywC3fp2O'
    ALGORITHM = 'HS256'
    jwt_expiration = 3600

settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)