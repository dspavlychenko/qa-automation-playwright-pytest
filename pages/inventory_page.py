from playwright.sync_api import expect

from pages.base_page import BasePage


class InventoryPage(BasePage):
    path = "/inventory.html"

    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test='inventory-item']")
        self.item_prices = page.locator("[data-test='inventory-item-price']")
        self.sort_select = page.locator("[data-test='product-sort-container']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def should_be_opened(self):
        expect(self.title).to_have_text("Products")

<<<<<<< HEAD
    def should_have_items(self, count: int):
        expect(self.items).to_have_count(count)

=======
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
    def add_to_cart(self, item_slug: str):
        self.page.locator(f"[data-test='add-to-cart-{item_slug}']").click()

    def sort_by(self, option_value: str):
        self.sort_select.select_option(option_value)
<<<<<<< HEAD
        expect(self.sort_select).to_have_value(option_value)  # wait until the sort is applied

    def prices(self) -> list[float]:
        """Read prices as they are right now. Call only after the page is ready (see sort_by / should_have_items)."""
=======

    def prices(self) -> list[float]:
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
        return [float(p.replace("$", "")) for p in self.item_prices.all_inner_texts()]

    def should_have_cart_count(self, count: int):
        expect(self.cart_badge).to_have_text(str(count))

    def open_cart(self):
        self.cart_link.click()
