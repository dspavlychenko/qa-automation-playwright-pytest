from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    path = "/"

    def __init__(self, page):
        super().__init__(page)
        self.username = page.locator("[data-test='username']")
        self.password = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error = page.locator("[data-test='error']")

    def login(self, user: str, password: str):
        self.username.fill(user)
        self.password.fill(password)
        self.login_button.click()

    def should_show_error(self, text: str):
        expect(self.error).to_contain_text(text)
