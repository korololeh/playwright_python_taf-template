from pytest import fixture
from playwright.sync_api import Browser, BrowserContext, sync_playwright
from typing import Any, Generator, Callable, Dict
from infrastructure.ui_page_objects.navigation import AutomationexerciseUI
from framework import AUTOMATIONEXERCISE_CONFIG
from os import environ

PW_HEADLESS = False  # Usually default is True. Set True to run in headless mode or override in Pycharm Run/Debug configuration
env_browsers = environ.get('BROWSERS', 'chromium,firefox').split(',')  # BROWSERS is a global var we'll need later for CI


def pytest_generate_tests(metafunc: Any):
    use_browsers = env_browsers
    metafunc.parametrize('bn', use_browsers, scope='session')  # Now you may invoke 'bn' param in tests to pass browser name


@fixture(scope='session')
def playwright() -> Generator[Any, None, None]:
    pw = sync_playwright().start()
    yield pw
    pw.stop()


@fixture(scope='session')
def launch_browser(playwright: Any, bn: str) -> Callable[[], Browser]:
    def launch(**kwargs: Dict[Any, Any]) -> Browser:
        launch_options = {'headless': PW_HEADLESS, **kwargs}
        browser = getattr(playwright, bn).launch(**launch_options)
        return browser
    return launch


@fixture(scope='session')
def browser(launch_browser: Callable[[], Browser]) -> Generator[Browser, None, None]:
    browser = launch_browser()
    yield browser
    browser.close()


@fixture(scope='class')
def browser_locale() -> str:
    return 'en'


@fixture(scope='function')
def context(browser: Browser, browser_locale: str) -> Generator[BrowserContext, None, None]:
    context_args = {'locale': browser_locale,
                    'accept_downloads': True,
                    'base_url': f'{AUTOMATIONEXERCISE_CONFIG["automationexercise_url"]}'}
    context = browser.new_context(**context_args)
    context.set_default_timeout(20_000)
    pages = []
    context.on('page', lambda p: pages.append(p))
    yield context
    context.close()


@fixture(scope='function')
def automationexercise_ui(context) -> AutomationexerciseUI:
    return AutomationexerciseUI(context.new_page())
