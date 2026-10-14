import pytest

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_e2e_checkout(logged_in, cart_page, checkout_page):
    logged_in.add_to_cart("sauce-labs-backpack")
    logged_in.open_cart()
    cart_page.should_have_items(1)
    cart_page.checkout()
    checkout_page.fill_info("Denys", "Tester", "01001")
    checkout_page.finish()
    checkout_page.should_be_completed()
