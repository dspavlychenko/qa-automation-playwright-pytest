import pytest

from api.booking_client import BookingClient
from api.graphql_client import GraphQLClient
from config.settings import API_PASSWORD, API_USER, PASSWORD, STANDARD_USER
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


# ---------- UI ----------
@pytest.fixture
def login_page(page):
    return LoginPage(page).open()


@pytest.fixture
def logged_in(page):
    """Logged-in user on the inventory page (reusable precondition)."""
    LoginPage(page).open().login(STANDARD_USER, PASSWORD)
    inventory = InventoryPage(page)
    inventory.should_be_opened()
    return inventory


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


# ---------- API ----------
@pytest.fixture(scope="session")
def booking_client():
    return BookingClient()


@pytest.fixture(scope="session")
def auth_client():
    client = BookingClient()
    client.auth(API_USER, API_PASSWORD)
    return client


@pytest.fixture
def booking_payload():
    return {
        "firstname": "Denys",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-11-01", "checkout": "2026-11-05"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def created_booking(booking_client, booking_payload, auth_client):
    """Test data prepared via API, cleaned up after the test."""
    resp = booking_client.create_booking(booking_payload)
    assert resp.status_code == 200
    booking_id = resp.json()["bookingid"]
    yield booking_id
    auth_client.delete_booking(booking_id)


@pytest.fixture(scope="session")
def graphql_client():
    return GraphQLClient()
