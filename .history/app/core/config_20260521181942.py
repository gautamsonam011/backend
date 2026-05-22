from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str

    APP_ENV: str

    DATABASE_URL: str

    REDIS_URL: str

    SECRET_KEY: str

    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    REFRESH_TOKEN_EXPIRE_DAYS: int

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()