import pytest

from api.booking_client import BookingClient
from config.settings import API_PASSWORD, API_USER, PASSWORD, STANDARD_USER
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


# ---------------- UI ----------------
@pytest.fixture
def login_page(page):
    return LoginPage(page).open()


@pytest.fixture
def inventory_page(page):
    """User is already logged in and sees the product list (waits until the page is ready)."""
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


# ---------------- API ----------------
@pytest.fixture(scope="session")
def api():
    """Client without token."""
    return BookingClient()


@pytest.fixture(scope="session")
def admin_api():
    """Client with auth token (can update and delete)."""
    client = BookingClient()
    client.auth(API_USER, API_PASSWORD)
    return client


@pytest.fixture
def new_booking():
    return {
        "firstname": "Denys",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-11-01", "checkout": "2026-11-05"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def booking_id(api, admin_api, new_booking):
    """Creates a booking before the test and deletes it after."""
    booking_id = api.create_booking(new_booking).json()["bookingid"]
    yield booking_id
    admin_api.delete_booking(booking_id)
