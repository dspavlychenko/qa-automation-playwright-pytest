import requests

from config.settings import API_BASE_URL, API_TIMEOUT


class BookingClient:
    """REST client for Restful-Booker API built on requests.Session.

    Every request goes through `_request`, so the timeout is applied in one place
    and a slow or sleeping Heroku dyno can never hang the test run.
    """

    def __init__(self, base_url: str = API_BASE_URL, timeout: float = API_TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})

    def _request(self, method: str, path: str, **kwargs) -> requests.Response:
        return self.session.request(method, f"{self.base_url}{path}", timeout=self.timeout, **kwargs)

    # ---------- health / auth ----------
    def ping(self) -> requests.Response:
        return self._request("GET", "/ping")

    def create_token(self, username: str, password: str) -> requests.Response:
        return self._request("POST", "/auth", json={"username": username, "password": password})

    def auth(self, username: str, password: str) -> str:
        resp = self.create_token(username, password)
        resp.raise_for_status()
        token = resp.json().get("token")
        if token:
            self.session.cookies.set("token", token)
        return token

    # ---------- CRUD ----------
    def get_booking_ids(self, **filters) -> requests.Response:
        return self._request("GET", "/booking", params=filters)

    def create_booking(self, payload: dict) -> requests.Response:
        return self._request("POST", "/booking", json=payload)

    def get_booking(self, booking_id: int) -> requests.Response:
        return self._request("GET", f"/booking/{booking_id}")

    def update_booking(self, booking_id: int, payload: dict) -> requests.Response:
        return self._request("PUT", f"/booking/{booking_id}", json=payload)

    def partial_update_booking(self, booking_id: int, payload: dict) -> requests.Response:
        return self._request("PATCH", f"/booking/{booking_id}", json=payload)

    def delete_booking(self, booking_id: int) -> requests.Response:
        return self._request("DELETE", f"/booking/{booking_id}")
