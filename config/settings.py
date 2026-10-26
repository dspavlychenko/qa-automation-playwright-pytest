import os

from dotenv import load_dotenv

load_dotenv()


def _env(name: str, default: str) -> str:
    """Env var with a default. Empty values (e.g. unset CI secrets) also fall back to the default."""
    return os.getenv(name) or default


UI_BASE_URL = _env("UI_BASE_URL", "https://www.saucedemo.com")
API_BASE_URL = _env("API_BASE_URL", "https://restful-booker.herokuapp.com")
API_TIMEOUT = float(_env("API_TIMEOUT", "15"))  # seconds, applied to every API request

STANDARD_USER = _env("STANDARD_USER", "standard_user")
LOCKED_USER = _env("LOCKED_USER", "locked_out_user")
PASSWORD = _env("UI_PASSWORD", "secret_sauce")

API_USER = _env("API_USER", "admin")
API_PASSWORD = _env("API_PASSWORD", "password123")
