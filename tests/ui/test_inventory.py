import pytest

pytestmark = pytest.mark.ui


def test_inventory_shows_six_products(logged_in):
    assert logged_in.items.count() == 6


@pytest.mark.parametrize("option, reverse", [("lohi", False), ("hilo", True)], ids=["price-asc", "price-desc"])
def test_sort_by_price(logged_in, option, reverse):
    logged_in.sort_by(option)
    prices = logged_in.prices()
    assert prices == sorted(prices, reverse=reverse)


def test_add_items_to_cart_updates_badge(logged_in):
    logged_in.add_to_cart("sauce-labs-backpack")
    logged_in.add_to_cart("sauce-labs-bike-light")
    logged_in.should_have_cart_count(2)
