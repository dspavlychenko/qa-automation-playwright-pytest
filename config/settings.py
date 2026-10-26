import os
<<<<<<< HEAD

=======
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
from dotenv import load_dotenv

load_dotenv()

<<<<<<< HEAD

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
=======
UI_BASE_URL = os.getenv("UI_BASE_URL", "https://www.saucedemo.com")
API_BASE_URL = os.getenv("API_BASE_URL", "https://restful-booker.herokuapp.com")
GRAPHQL_URL = os.getenv("GRAPHQL_URL", "https://countries.trevorblades.com/")

STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
LOCKED_USER = os.getenv("LOCKED_USER", "locked_out_user")
PASSWORD = os.getenv("UI_PASSWORD", "secret_sauce")

API_USER = os.getenv("API_USER", "admin")
API_PASSWORD = os.getenv("API_PASSWORD", "password123")
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
