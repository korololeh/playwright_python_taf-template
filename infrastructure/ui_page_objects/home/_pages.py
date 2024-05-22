from playwright.sync_api import Page
from framework.ui_object_tools import BasePage
from . import _locators as l


class HomePage(BasePage):
    def __init__(self, tab: Page):
        super().__init__(tab)

    @property
    def title(self) -> str:
        return self.tab.title()

    @property
    def nav_bar_is_visible(self) -> bool:
        return self.tab.is_visible(l.nav_bar)
