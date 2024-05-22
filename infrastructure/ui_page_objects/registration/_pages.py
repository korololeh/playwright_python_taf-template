from playwright.sync_api import Page
from framework.ui_object_tools import BasePage
import infrastructure.ui_page_objects as p
from . import _locators as l


class RegistrationPage(BasePage):

    def __init__(self, tab: Page):
        super().__init__(tab)

    def fill_registration_form(self, user_data):
        self.tab.click(l.gender)
        self.tab.fill(l.password_input, user_data["password"])
        self.tab.select_option(l.day, user_data["day"])
        self.tab.select_option(l.month, user_data["month"])
        self.tab.select_option(l.year, user_data["year"])
        self.tab.fill(l.first_name, user_data["first_name"])
        self.tab.fill(l.last_name, user_data["last_name"])
        self.tab.fill(l.company, user_data["company"])
        self.tab.fill(l.address1, user_data["address1"])
        self.tab.select_option(l.country, user_data["country"])
        self.tab.fill(l.state, user_data["state"])
        self.tab.fill(l.city, user_data["city"])
        self.tab.fill(l.zipcode, user_data["zip_code"])
        self.tab.fill(l.mobile_number, user_data["phone"])
        self.tab.click(l.create_account_button)

    def account_created(self):
        return self.tab.locator(l.account_created_message).inner_text() == "ACCOUNT CREATED!"

    def user_name_and_email_is_prefilled(self, user_data) -> bool:
        return (self.tab.locator(l.name_input).get_attribute("value") == user_data["name"] and
                self.tab.locator(l.email_input).get_attribute("value") == user_data["email"])

