from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Define your settings here
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str = "mysecretkey"

settings = Settings()
