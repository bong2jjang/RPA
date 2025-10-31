"""
@BE Configuration Module
환경 변수 기반 설정 관리
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """
    @BE 애플리케이션 설정 클래스
    환경 변수를 통해 설정 값을 로드
    """

    # Application Settings
    APP_NAME: str = "AI Multilingual Management System"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Database Settings
    DB_URL: str = "sqlite:///./ai_multilang.db"
    DB_ECHO: bool = False

    # Redis Settings
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_TIMEOUT: int = 300

    # AI API Settings
    AI_API_KEY: Optional[str] = None
    AI_API_URL: Optional[str] = None
    AI_MODEL: str = "gpt-4"

    # Security Settings
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS Settings
    CORS_ORIGINS: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000"
    ]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# 설정 인스턴스 생성
settings = Settings()


def get_settings() -> Settings:
    """
    @BE 설정 객체 반환
    의존성 주입에 사용
    """
    return settings
