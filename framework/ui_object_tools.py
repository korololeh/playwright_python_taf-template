from playwright.sync_api import Page
from infrastructure.maps.error_map import BrowserConsoleErrorMap

DEFAULT_LOCATOR_TIMEOUT = 5000
console_error_msg_map = BrowserConsoleErrorMap().br_console_error_msg_map


class BasePage:

    def __init__(self, tab: Page):
        self.tab = tab
        self.tab.on('console', console_error_msg_filter)

    def contains_text(self, text: str, /) -> bool:
        return bool(self.tab.query_selector(f':has-text("{text}")'))


def console_error_msg_filter(msg):
    """
    Populate method when browser console error filtering required
    """
    if msg.type == 'error':
        pass
