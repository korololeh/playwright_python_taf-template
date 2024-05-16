from playwright.sync_api import Page


class SignUpForm:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.gender = page.locator("xpath=//*[@id='uniform-id_gender1']")
        self.name = page.locator("xpath=//input[@name='name']")
        self.email = page.locator("xpath=//input[@data-qa='email']")
        self.password = page.locator("xpath=//*[@id='password']")
        self.day = page.locator("xpath=//*[@id='days']")
        self.month = page.locator("xpath=//*[@id='months']")
        self.year = page.locator("xpath=//*[@id='years']")
        self.first_name = page.locator("xpath=//*[@id='first_name']")
        self.last_name = page.locator("xpath=//*[@id='last_name']")
        self.company = page.locator("xpath=//*[@id='company']")
        self.address1 = page.locator("xpath=//*[@id='address1']")
        self.country = page.locator("xpath=//*[@id='country']")
        self.state = page.locator("xpath=//*[@id='state']")
        self.city = page.locator("xpath=//*[@id='city']")
        self.zipcode = page.locator("xpath=//*[@id='zipcode']")
        self.zipcode = page.locator("xpath=//*[@id='zipcode']")
        self.mobile_number = page.locator("xpath=//*[@id='mobile_number']")
        self.create_btn = page.locator("xpath=//button[@data-qa='create-account']")

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
