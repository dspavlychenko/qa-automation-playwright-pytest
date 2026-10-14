import os
from dotenv import load_dotenv

load_dotenv()

UI_BASE_URL = os.getenv("UI_BASE_URL", "https://www.saucedemo.com")
API_BASE_URL = os.getenv("API_BASE_URL", "https://restful-booker.herokuapp.com")
GRAPHQL_URL = os.getenv("GRAPHQL_URL", "https://countries.trevorblades.com/")

STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
LOCKED_USER = os.getenv("LOCKED_USER", "locked_out_user")
PASSWORD = os.getenv("UI_PASSWORD", "secret_sauce")

API_USER = os.getenv("API_USER", "admin")
API_PASSWORD = os.getenv("API_PASSWORD", "password123")
