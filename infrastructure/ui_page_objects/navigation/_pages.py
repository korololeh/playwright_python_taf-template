from playwright.sync_api import Page
import infrastructure.ui_page_objects as p
from . import _locators as l


class PlaywrightUI:
    """
    Central directory for all pages which passes the Page
    """
    def __init__(self, tab: Page):
        self.tab = tab

    @property
    def current_page_title(self) -> str:
        return self.tab.title()

    @property
    def home_tab(self) -> p.HomePage:
        self.tab.click(l.home_page_link)
        return p.HomePage(self.tab)
