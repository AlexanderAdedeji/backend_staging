import os
from pydantic import BaseSettings
from pathlib import Path



class Settings(BaseSettings):
    APP_NAME:str
    DEVELOPMENT_DATABASE_URL:str
    PRODUCTION_DATABASE_URL:str
    DEBUG:bool
    REJECTED:str
    GOOD:str
    class Config:
        env_file =os.getenv(
            "ENV_VARIABLE_PATH", Path(__file__).parent / "ENV/.env"
        )