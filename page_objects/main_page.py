from playwright.sync_api import Page


class MainPage:
    URL = "/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.title()
        self.login_btn = page.locator("xpath=//a[@href='/login']")

    def load(self) -> None:
        self.page.goto(self.URL)
        assert self.page.title() == "Automation Exercise"

    def click_login(self) -> None:
        self.login_btn.is_enabled()
        self.login_btn.click()
