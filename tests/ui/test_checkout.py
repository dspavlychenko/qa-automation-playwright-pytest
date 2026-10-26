import allure
import pytest

pytestmark = pytest.mark.ui


@allure.feature("Checkout")
@allure.story("Happy path")
@pytest.mark.smoke
def test_buy_one_item(inventory_page, cart_page, checkout_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    cart_page.checkout()
    checkout_page.fill_info("Denys", "Tester", "01001")
    checkout_page.finish()

    checkout_page.should_be_completed()
