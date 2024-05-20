from framework.utils import generate_user_data


class TestUserRegistration:
    def test_user_registration_success(self, playwright_ui):
        registration_page = playwright_ui.registration_tab
        registration_page.fill_registration_form(generate_user_data())

        assert registration_page.account_created

        # main_page.load()
        # main_page.click_login()
        # login_sign_up_page.is_loaded()
        # login_sign_up_page.fill_sign_up(user_data["name"], user_data["email"])
        # registration_page.fill_registration_form(user_data)
        #
        # assert page.locator("xpath=//h2[@data-qa='account-created']").inner_text() == "ACCOUNT CREATED!"
