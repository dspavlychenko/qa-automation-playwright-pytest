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

    def open(self):
        super().open()
        expect(self.login_button).to_be_visible()  # page is interactive before the test starts typing
        return self

    def login(self, user: str, password: str):
        self.username.fill(user)
        self.password.fill(password)
        self.login_button.click()

    def should_show_error(self, text: str):
        expect(self.error).to_contain_text(text)

    def should_mask_password(self):
        expect(self.password).to_have_attribute("type", "password")
