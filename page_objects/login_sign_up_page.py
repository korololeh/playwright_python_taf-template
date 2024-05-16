from playwright.sync_api import Page


class SignUpInPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.sign_up_name = page.locator("xpath=//input[@name='name']")
        self.sign_up_email = page.locator("xpath=//input[@data-qa='signup-email']")
        self.sign_up_btn = page.locator("xpath=//button[@data-qa='signup-button']")

    def is_loaded(self) -> None:
        assert self.sign_up_name.is_visible()
        assert self.sign_up_email.is_visible()
        assert self.sign_up_btn.is_visible()

    def fill_sign_up(self, user_name, user_mail) -> None:
        self.sign_up_name.fill(user_name)
        self.sign_up_email.fill(user_mail)
        self.sign_up_btn.click()
