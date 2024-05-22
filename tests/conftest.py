from pytest import fixture
from infrastructure.ui_page_objects.navigation import PlaywrightUI


@fixture(scope='function')
def playwright_ui(context) -> PlaywrightUI:
    return PlaywrightUI(context.new_page())
