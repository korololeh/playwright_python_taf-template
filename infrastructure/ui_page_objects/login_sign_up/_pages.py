from playwright.sync_api import Page
from framework.ui_object_tools import BasePage
import infrastructure.ui_page_objects as p
from . import _locators as l


class LoginSignUp(BasePage):

    def __init__(self, tab: Page) -> None:
        super().__init__(tab)
        # self.sign_up_name = page.locator(LoginSignUpPageLocators.SIGN_UP_NAME)
        # self.sign_up_email = page.locator(LoginSignUpPageLocators.SIGN_UP_EMAIL)
        # self.sign_up_btn = page.locator(LoginSignUpPageLocators.SIGN_UP_BTN)

    @property
    def title(self) -> str:
        return self.tab.title()

    # def is_loaded(self) -> None:
    #     assert self.sign_up_name.is_visible()
    #     assert self.sign_up_email.is_visible()
    #     assert self.sign_up_btn.is_visible()
    #
    # def fill_sign_up(self, user_name, user_mail) -> None:
    #     self.sign_up_name.fill(user_name)
    #     self.sign_up_email.fill(user_mail)
    #     self.sign_up_btn.click()
