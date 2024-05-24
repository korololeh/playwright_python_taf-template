from framework.utils import generate_user_data


class TestUserRegistration:
    def test_sing_up_page_is_visible(self, automationexercise_ui):
        login_sign_up_page = automationexercise_ui.login_sign_up_tab

        assert login_sign_up_page.login_sign_up_is_visible

    def test_open_sign_up_page_and_verify_user_info(self, automationexercise_ui):
        user_data = generate_user_data()
        registration_page = automationexercise_ui.login_sign_up_tab.fill_sign_up(user_data["name"], user_data["email"])

        assert registration_page.user_name_is_populated(user_data["name"])
        assert registration_page.user_email_is_populated(user_data["email"])

    def test_account_is_created(self, automationexercise_ui):
        user_data = generate_user_data()
        registration_page = automationexercise_ui.login_sign_up_tab.fill_sign_up(user_data["name"], user_data["email"])
        registration_page.fill_registration_form(user_data)

        assert registration_page.account_created()
