from playwright.sync_api import Page
import infrastructure.ui_page_objects as p
from . import _locators as l


class AutomationexerciseUI:
    """
    Central directory for all pages which passes the Page
    """

    def __init__(self, tab: Page):
        self.tab = tab
        self.tab.goto("/")

    @property
    def current_page_title(self) -> str:
        return self.tab.title()

    @property
    def home_tab(self) -> p.HomePage:
        self.tab.click(l.home_page_nav)
        return p.HomePage(self.tab)

    @property
    def login_sign_up_tab(self) -> p.LoginSignUpPage:
        self.tab.click(l.login_sign_up_link)
        return p.LoginSignUpPage(self.tab)
