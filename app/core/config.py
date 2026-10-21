from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Generic POC Backend"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite:///./poc.db"
    RESET_DB_ON_STARTUP: bool = False
    ALLOWED_ORIGINS: str = "*"

    AI_PROVIDER: str = "mock"  # Options: mock, openai, gemini
    AI_MODEL_API_KEY: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()