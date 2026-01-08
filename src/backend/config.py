import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "TaskMastery API"
    API_VERSION: str = "v1"
    ALLOWED_ORIGINS: list = ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:8000"]
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"


settings = Settings()