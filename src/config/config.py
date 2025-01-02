from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")


class Config:

    PROJECT_DIR = Path(__file__).resolve().parent.parent
    SRC_DIR = PROJECT_DIR / "src"
    DB_DIR = SRC_DIR / "db"
    MODELS_DIR = SRC_DIR / "models"
    SCHEMAS_DIR = SRC_DIR / "schemas"
    CONFIG_DIR = SRC_DIR / "config"
    UTILS_DIR = SRC_DIR / "utils"

