from playwright.sync_api import Page

from x_pages.base_page import BasePage
from x_locators import LoginSignUpPageLocators


class SignUpInPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.sign_up_name = page.locator(LoginSignUpPageLocators.SIGN_UP_NAME)
        self.sign_up_email = page.locator(LoginSignUpPageLocators.SIGN_UP_EMAIL)
        self.sign_up_btn = page.locator(LoginSignUpPageLocators.SIGN_UP_BTN)

    def is_loaded(self) -> None:
        assert self.sign_up_name.is_visible()
        assert self.sign_up_email.is_visible()
        assert self.sign_up_btn.is_visible()

    def fill_sign_up(self, user_name, user_mail) -> None:
        self.sign_up_name.fill(user_name)
        self.sign_up_email.fill(user_mail)
        self.sign_up_btn.click()
