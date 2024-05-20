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
        # Usually after the click we are checking on expected activities within executing function
        # e.g. self.tab.locator(l.working_indicator).wait_for(state='hidden')
        # or we may use context manager to expect some network activities like:
        # with self.tab.expect_response('**/MASK_FOR/YOUR_RESPONSE/**.json'): action_to_execute
        return p.HomePage(self.tab)

    @property
    def login_sign_up_tab(self) -> p.LoginSignUpPage:
        self.tab.click(l.login_sign_up_link)
        return p.LoginSignUpPage(self.tab)

    @property
    def registration_tab(self) -> p.RegistrationPage:
        self.tab.click(l.registration_page_link)
        return p.RegistrationPage(self.tab)
