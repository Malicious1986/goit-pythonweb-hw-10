import os
from pathlib import Path

try:
    from dotenv import load_dotenv

    _env_path = Path(".") / ".env"
    if _env_path.exists():
        load_dotenv(dotenv_path=_env_path)
except Exception:
    pass


class Config:

    DB_URL = os.getenv(
        "DB_URL",
        "postgresql+asyncpg://postgres:567234@localhost:5432/contacts",
    )


config = Config
