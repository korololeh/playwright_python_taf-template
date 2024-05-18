from playwright.sync_api import Page
from page_objects.pages.main_page import MainPage
from page_objects.pages.login_sign_up_page import SignUpInPage
from page_objects.pages.registration_page import SignUpForm
from utils.string_utils import generate_user_data

user_data = generate_user_data()


def test_register_user(page: Page,
                       main_page: MainPage,
                       login_sign_up_page: SignUpInPage,
                       registration_page: SignUpForm) -> None:
    main_page.load()
    main_page.click_login()
    login_sign_up_page.is_loaded()
    login_sign_up_page.fill_sign_up(user_data["name"], user_data["email"])
    registration_page.fill_registration_form(user_data)
    assert page.locator("xpath=//h2[@data-qa='account-created']").inner_text() == "ACCOUNT CREATED!"
