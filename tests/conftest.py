import pytest
from page_objects.pages.main_page import MainPage
from page_objects.pages.login_sign_up_page import SignUpInPage
from page_objects.pages.registration_page import SignUpForm
from playwright.sync_api import Page


@pytest.fixture
def main_page(page: Page) -> MainPage:
    return MainPage(page)


@pytest.fixture
def login_sign_up_page(page: Page) -> SignUpInPage:
    return SignUpInPage(page)


@pytest.fixture
def registration_page(page: Page) -> SignUpForm:
    return SignUpForm(page)
