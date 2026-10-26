import allure
import pytest

from config.settings import LOCKED_USER, PASSWORD, STANDARD_USER
from pages.inventory_page import InventoryPage

pytestmark = pytest.mark.ui

NOT_MATCHING = "do not match any user"

INVALID_CREDENTIALS = [
    pytest.param(STANDARD_USER, "wrong_password", NOT_MATCHING, id="wrong-password"),
    pytest.param("no_such_user", PASSWORD, NOT_MATCHING, id="unknown-user"),
    pytest.param("", PASSWORD, "Username is required", id="empty-username"),
    pytest.param(STANDARD_USER, "", "Password is required", id="empty-password"),
    pytest.param("", "", "Username is required", id="both-empty"),
    pytest.param(STANDARD_USER.upper(), PASSWORD, NOT_MATCHING, id="username-is-case-sensitive"),
    pytest.param(STANDARD_USER, PASSWORD.upper(), NOT_MATCHING, id="password-is-case-sensitive"),
    pytest.param("' OR 1=1 --", "' OR 1=1 --", NOT_MATCHING, id="sql-injection-string"),
]


@allure.feature("Authentication")
@allure.story("Successful login")
@pytest.mark.smoke
def test_login_success(login_page, page):
    login_page.login(STANDARD_USER, PASSWORD)

    InventoryPage(page).should_be_opened()


@allure.feature("Authentication")
@allure.story("Invalid credentials")
@pytest.mark.parametrize(("username", "password", "error"), INVALID_CREDENTIALS)
def test_login_invalid_credentials(login_page, username, password, error):
    login_page.login(username, password)

    login_page.should_show_error(error)


@allure.feature("Authentication")
@allure.story("Locked account")
def test_login_locked_user(login_page):
    login_page.login(LOCKED_USER, PASSWORD)

    login_page.should_show_error("this user has been locked out")


@allure.feature("Authentication")
@allure.story("Security")
def test_password_field_is_masked(login_page):
    login_page.should_mask_password()
