from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    UPLOAD_DIR: str

    OLLAMA_CHAT_MODEL: str
    OLLAMA_EMBEDDING_MODEL: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()
DATABASE_URL = settings.DATABASE_URL
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
UPLOAD_DIR = settings.UPLOAD_DIR
OLLAMA_CHAT_MODEL = settings.OLLAMA_CHAT_MODEL
OLLAMA_EMBEDDING_MODEL = settings.OLLAMA_EMBEDDING_MODEL