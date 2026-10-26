import allure
import pytest

pytestmark = pytest.mark.ui

BACKPACK = "sauce-labs-backpack"
BIKE_LIGHT = "sauce-labs-bike-light"


@allure.feature("Cart")
@allure.story("Cart badge")
@pytest.mark.parametrize("items", [[BACKPACK], [BACKPACK, BIKE_LIGHT]], ids=["one-item", "two-items"])
def test_cart_badge_counts_added_items(inventory_page, items):
    for item in items:
        inventory_page.add_to_cart(item)

    inventory_page.should_have_cart_count(len(items))


@allure.feature("Cart")
@allure.story("Cart contents")
def test_cart_shows_added_item(inventory_page, cart_page):
    inventory_page.add_to_cart(BACKPACK)
    inventory_page.open_cart()

    cart_page.should_have_items(1)
