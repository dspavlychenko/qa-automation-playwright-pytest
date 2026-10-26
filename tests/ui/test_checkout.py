<<<<<<< HEAD
import allure
=======
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
import pytest

pytestmark = pytest.mark.ui


<<<<<<< HEAD
@allure.feature("Checkout")
@allure.story("Happy path")
@pytest.mark.smoke
def test_buy_one_item(inventory_page, cart_page, checkout_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    cart_page.checkout()
    checkout_page.fill_info("Denys", "Tester", "01001")
    checkout_page.finish()

=======
@pytest.mark.smoke
def test_e2e_checkout(logged_in, cart_page, checkout_page):
    logged_in.add_to_cart("sauce-labs-backpack")
    logged_in.open_cart()
    cart_page.should_have_items(1)
    cart_page.checkout()
    checkout_page.fill_info("Denys", "Tester", "01001")
    checkout_page.finish()
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
    checkout_page.should_be_completed()
