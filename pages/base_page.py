<<<<<<< HEAD
from playwright.sync_api import Page
=======
from playwright.sync_api import Page, expect
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7

from config.settings import UI_BASE_URL


class BasePage:
    """Common actions for all pages. No hard sleeps: Playwright auto-waits."""

    path = "/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(UI_BASE_URL + self.path)
        return self
<<<<<<< HEAD
=======

    def should_have_url(self, part: str):
        expect(self.page).to_have_url(f"{UI_BASE_URL}{part}")
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
