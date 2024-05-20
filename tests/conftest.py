from pytest import fixture
from infrastructure.ui_page_objects.navigation import PlaywrightUI


@fixture(scope='function')
def playwright_ui(context) -> PlaywrightUI:
    return PlaywrightUI(context.new_page())

# @fixture
# def main_page(page: Page) -> MainPage:
#     return MainPage(page)
#
#
# @fixture
# def login_sign_up_page(page: Page) -> SignUpInPage:
#     return SignUpInPage(page)
#
#
# @fixture
# def registration_page(page: Page) -> SignUpForm:
#     return SignUpForm(page)
