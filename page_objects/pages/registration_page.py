from playwright.sync_api import Page

from page_objects.pages.base_page import BasePage
from page_objects.locators.registration_page_locators import RegistrationPageLocators


class SignUpForm(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.gender = page.locator(RegistrationPageLocators.GENDER)
        self.name = page.locator(RegistrationPageLocators.NAME)
        self.email = page.locator(RegistrationPageLocators.EMAIL)
        self.password = page.locator(RegistrationPageLocators.PASSWORD)
        self.day = page.locator(RegistrationPageLocators.DAY)
        self.month = page.locator(RegistrationPageLocators.MONTH)
        self.year = page.locator(RegistrationPageLocators.YEAR)
        self.first_name = page.locator(RegistrationPageLocators.FIRST_NAME)
        self.last_name = page.locator(RegistrationPageLocators.LAST_NAME)
        self.company = page.locator(RegistrationPageLocators.COMPANY)
        self.address1 = page.locator(RegistrationPageLocators.ADDRESS1)
        self.country = page.locator(RegistrationPageLocators.COUNTRY)
        self.state = page.locator(RegistrationPageLocators.STATE)
        self.city = page.locator(RegistrationPageLocators.CITY)
        self.zipcode = page.locator(RegistrationPageLocators.ZIPCODE)
        self.mobile_number = page.locator(RegistrationPageLocators.MOBILE_NUMBER)
        self.create_btn = page.locator(RegistrationPageLocators.CREATE_BTN)

    def fill_registration_form(self, user_data) -> None:
        self.gender.click()
        self.password.fill(user_data["password"])
        self.day.select_option(user_data["day"])
        self.month.select_option(user_data["month"])
        self.year.select_option(user_data["year"])
        self.first_name.fill(user_data["first_name"])
        self.last_name.fill(user_data["last_name"])
        self.company.fill(user_data["company"])
        self.address1.fill(user_data["address1"])
        self.country.select_option(user_data["country"])
        self.state.fill(user_data["state"])
        self.city.fill(user_data["city"])
        self.zipcode.fill(user_data["zip_code"])
        self.mobile_number.fill(user_data["phone"])

        assert self.gender.is_checked()
        assert self.name.get_attribute("value") == user_data["name"]
        assert self.email.get_attribute("value") == user_data["email"]
        assert self.day.input_value() == user_data["day"]
        assert self.month.input_value() == user_data["month"]
        assert self.year.input_value() == user_data["year"]
        assert self.country.input_value() == user_data["country"]

        self.create_btn.click()
