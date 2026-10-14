from playwright.sync_api import Page, expect

from config.settings import UI_BASE_URL


class BasePage:
    """Common actions for all pages. No hard sleeps: Playwright auto-waits."""

    path = "/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(UI_BASE_URL + self.path)
        return self

    def should_have_url(self, part: str):
        expect(self.page).to_have_url(f"{UI_BASE_URL}{part}")
