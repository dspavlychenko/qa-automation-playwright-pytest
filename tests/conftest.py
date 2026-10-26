import pytest

from api.booking_client import BookingClient
<<<<<<< HEAD
=======
from api.graphql_client import GraphQLClient
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
from config.settings import API_PASSWORD, API_USER, PASSWORD, STANDARD_USER
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

<<<<<<< HEAD
# ---------------- UI ----------------

=======

# ---------- UI ----------
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
@pytest.fixture
def login_page(page):
    return LoginPage(page).open()


@pytest.fixture
<<<<<<< HEAD
def inventory_page(page):
    """User is already logged in and sees the product list (waits until the page is ready)."""
=======
def logged_in(page):
    """Logged-in user on the inventory page (reusable precondition)."""
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
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


<<<<<<< HEAD
# ---------------- API ----------------

@pytest.fixture(scope="session")
def api():
    """Client without token."""
=======
# ---------- API ----------
@pytest.fixture(scope="session")
def booking_client():
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
    return BookingClient()


@pytest.fixture(scope="session")
<<<<<<< HEAD
def admin_api():
    """Client with auth token (can update and delete)."""
=======
def auth_client():
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
    client = BookingClient()
    client.auth(API_USER, API_PASSWORD)
    return client


@pytest.fixture
<<<<<<< HEAD
def new_booking():
=======
def booking_payload():
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
    return {
        "firstname": "Denys",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-11-01", "checkout": "2026-11-05"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
<<<<<<< HEAD
def booking_id(api, admin_api, new_booking):
    """Creates a booking before the test and deletes it after."""
    booking_id = api.create_booking(new_booking).json()["bookingid"]
    yield booking_id
    admin_api.delete_booking(booking_id)
=======
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
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
