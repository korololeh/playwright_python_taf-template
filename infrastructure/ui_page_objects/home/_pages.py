from playwright.sync_api import Page
from framework.ui_object_tools import BasePage
import infrastructure.ui_page_objects as p
from . import _locators as l


class HomePage(BasePage):
    URL = "/"

    def __init__(self, tab: Page):
        super().__init__(tab)

    @property
    def title(self) -> str:
        return self.tab.title()

    def load(self):
        self.tab.goto(self.URL)

    def click_login(self):
        self.tab.click(l.login_button)

