from playwright.sync_api import Page

from page_objects.pages.base_page import BasePage
from page_objects.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    URL = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title = page.title()
        self.login_btn = page.locator(MainPageLocators.LOGIN_BTN)

    def load(self) -> None:
        self.page.goto(self.URL)
        # assert self.page.title() == "Automation Exercise"

    def click_login(self) -> None:
        # self.login_btn.is_enabled()
        self.login_btn.click()
