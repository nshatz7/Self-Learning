from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application Metadata (used in FastAPI instantiation)
    PROJECT_NAME: str = "Lead Management API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Backend API for managing customer leads, users, and activity."
    
    # Environment
    ENVIRONMENT: str = "development"

    # CORS Origins (used by CORSMiddleware in main.py)
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:8000",
    ]

    # Tells Pydantic to read variables from a .env file in your root directory
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignores extra variables in .env not defined here yet
    )


# Instantiate a single settings object to import across your app
settings = Settings()
