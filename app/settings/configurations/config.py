import os
from pydantic import BaseSettings
from pathlib import Path



class Settings(BaseSettings):
    APP_NAME:str
    DEVELOPMENT_DATABASE_URL:str
    DATABASE_URL:str
    DEBUG:bool

    class Config:
        env_file =os.getenv(
            "ENV_VARIABLE_PATH", Path(__file__).parent / "ENV/.env"
        )