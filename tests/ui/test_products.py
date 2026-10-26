import allure
import pytest

pytestmark = pytest.mark.ui


@allure.feature("Products")
@allure.story("Product list")
def test_products_list_has_6_items(inventory_page):
    inventory_page.should_have_items(6)


@allure.feature("Products")
@allure.story("Sorting")
@pytest.mark.parametrize(
    ("option", "descending"),
    [("lohi", False), ("hilo", True)],
    ids=["price-low-to-high", "price-high-to-low"],
)
def test_sort_by_price(inventory_page, option, descending):
    inventory_page.sort_by(option)

    prices = inventory_page.prices()
    assert prices == sorted(prices, reverse=descending)
