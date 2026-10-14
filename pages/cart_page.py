from playwright.sync_api import expect

from pages.base_page import BasePage


class CartPage(BasePage):
    path = "/cart.html"

    def __init__(self, page):
        super().__init__(page)
        self.items = page.locator("[data-test='inventory-item']")
        self.checkout_button = page.locator("[data-test='checkout']")

    def should_have_items(self, count: int):
        expect(self.items).to_have_count(count)

    def checkout(self):
        self.checkout_button.click()
