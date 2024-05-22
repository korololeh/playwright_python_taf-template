from framework.utils import generate_user_data


class TestUserRegistration:
    def test_home_page_is_loaded(self, playwright_ui):
        home_page = playwright_ui.home_tab
        assert home_page.nav_bar_visible

    def test_sing_up_page_is_visible(self, playwright_ui):
        login_sign_up_page = playwright_ui.login_sign_up_tab
        assert login_sign_up_page.login_sign_up_is_visible

    def test_open_sign_up_page_and_verify_user_info(self, playwright_ui):
        user_data = generate_user_data()
        login_sign_up_page = playwright_ui.login_sign_up_tab
        registration_page = login_sign_up_page.fill_sign_up(user_data)
        assert registration_page.user_name_and_email_is_prefilled(user_data)

    def test_account_is_created(self, playwright_ui):
        user_data = generate_user_data()
        login_sign_up_page = playwright_ui.login_sign_up_tab
        registration_page = login_sign_up_page.fill_sign_up(user_data)
        registration_page.fill_registration_form(user_data)
        assert registration_page.account_created()