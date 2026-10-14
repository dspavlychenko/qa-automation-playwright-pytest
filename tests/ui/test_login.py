import pytest

from config.settings import LOCKED_USER, PASSWORD, STANDARD_USER
from pages.inventory_page import InventoryPage

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_login_with_valid_credentials(login_page, page):
    login_page.login(STANDARD_USER, PASSWORD)
    InventoryPage(page).should_be_opened()


def test_locked_out_user_cannot_login(login_page):
    login_page.login(LOCKED_USER, PASSWORD)
    login_page.should_show_error("Sorry, this user has been locked out")


@pytest.mark.parametrize(
    "user, password, error",
    [
        ("", PASSWORD, "Username is required"),
        (STANDARD_USER, "", "Password is required"),
        (STANDARD_USER, "wrong_password", "do not match any user"),
    ],
    ids=["empty-username", "empty-password", "wrong-password"],
)
def test_login_negative(login_page, user, password, error):
    login_page.login(user, password)
    login_page.should_show_error(error)
