from playwright.sync_api import Page
from framework.ui_object_tools import BasePage
import infrastructure.ui_page_objects as p
from . import _locators as l


class RegistrationPage(BasePage):

    def __init__(self, tab: Page):
        super().__init__(tab)
        # self.gender = page.locator(RegistrationPageLocators.GENDER)
        # self.name = page.locator(RegistrationPageLocators.NAME)
        # self.email = page.locator(RegistrationPageLocators.EMAIL)
        # self.password = page.locator(RegistrationPageLocators.PASSWORD)
        # self.day = page.locator(RegistrationPageLocators.DAY)
        # self.month = page.locator(RegistrationPageLocators.MONTH)
        # self.year = page.locator(RegistrationPageLocators.YEAR)
        # self.first_name = page.locator(RegistrationPageLocators.FIRST_NAME)
        # self.last_name = page.locator(RegistrationPageLocators.LAST_NAME)
        # self.company = page.locator(RegistrationPageLocators.COMPANY)
        # self.address1 = page.locator(RegistrationPageLocators.ADDRESS1)
        # self.country = page.locator(RegistrationPageLocators.COUNTRY)
        # self.state = page.locator(RegistrationPageLocators.STATE)
        # self.city = page.locator(RegistrationPageLocators.CITY)
        # self.zipcode = page.locator(RegistrationPageLocators.ZIPCODE)
        # self.mobile_number = page.locator(RegistrationPageLocators.MOBILE_NUMBER)
        # self.create_btn = page.locator(RegistrationPageLocators.CREATE_BTN)

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

        # assert self.gender.is_checked()
        # assert self.name.get_attribute("value") == user_data["name"]
        # assert self.email.get_attribute("value") == user_data["email"]
        # assert self.day.input_value() == user_data["day"]
        # assert self.month.input_value() == user_data["month"]
        # assert self.year.input_value() == user_data["year"]
        # assert self.country.input_value() == user_data["country"]

    def account_created(self):
        return self.tab.locator(l.account_created_message).inner_text() == "ACCOUNT CREATED!"
