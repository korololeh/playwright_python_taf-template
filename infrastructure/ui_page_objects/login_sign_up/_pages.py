from playwright.sync_api import Page
from framework.ui_object_tools import BasePage
from infrastructure.ui_page_objects.registration import RegistrationPage
from . import _locators as l


class LoginSignUpPage(BasePage):

    def __init__(self, tab: Page):
        super().__init__(tab)

    @property
    def title(self) -> str:
        return self.tab.title()

    @property
    def login_sign_up_is_visible(self) -> bool:
        return self.tab.is_visible(l.sign_up_button)

    def fill_sign_up(self, name, email) -> RegistrationPage:
        self.tab.fill(l.sign_up_name, name)
        self.tab.fill(l.sign_up_email, email)
        self.tab.click(l.sign_up_button)
        return RegistrationPage(self.tab)

