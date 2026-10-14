import requests

from config.settings import API_BASE_URL


class BookingClient:
    """Thin wrapper over Restful-Booker API built on requests.Session."""

    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def auth(self, username: str, password: str) -> str:
        resp = self.session.post(f"{self.base_url}/auth", json={"username": username, "password": password})
        resp.raise_for_status()
        token = resp.json().get("token")
        if token:
            self.session.cookies.set("token", token)
        return token

    def create_booking(self, payload: dict) -> requests.Response:
        return self.session.post(f"{self.base_url}/booking", json=payload)

    def get_booking(self, booking_id: int) -> requests.Response:
        return self.session.get(f"{self.base_url}/booking/{booking_id}")

    def update_booking(self, booking_id: int, payload: dict) -> requests.Response:
        return self.session.put(f"{self.base_url}/booking/{booking_id}", json=payload)

    def delete_booking(self, booking_id: int) -> requests.Response:
        return self.session.delete(f"{self.base_url}/booking/{booking_id}")
