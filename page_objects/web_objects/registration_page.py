from selenium.webdriver.common.by import By

first_name_field = (By.ID, "customer.firstName")
last_name_field = (By.ID, "customer.lastName")
address_field = (By.ID, "customer.address.street")
city_field = (By.ID, "customer.address.city")
state_field = (By.ID, "customer.address.state")
zip_code_field = (By.ID, "customer.address.zipCode")
phone_number_field = (By.ID, "customer.phoneNumber")
ssn_field = (By.ID, "customer.ssn")
username_field = (By.ID, "customer.username")
password_field = (By.ID, "customer.password")
password_confirmation_field = (By.ID, "repeatedPassword")
register_button = (By.XPATH, "//table[@class='form2']//input[@class='button']")
registration_subtitle = (By.XPATH, "//div[@id='rightPanel']/p")


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def get_first_name_field(self):
        return self.driver.find_element(first_name_field[0], first_name_field[1])

    def get_last_name_field(self):
        return self.driver.find_element(last_name_field[0], last_name_field[1])

    def get_address_field(self):
        return self.driver.find_element(address_field[0], address_field[1])

    def get_city_field(self):
        return self.driver.find_element(city_field[0], city_field[1])

    def get_state_field(self):
        return self.driver.find_element(state_field[0], state_field[1])

    def get_zip_code_field(self):
        return self.driver.find_element(zip_code_field[0], zip_code_field[1])

    def get_phone_number_field(self):
        return self.driver.find_element(phone_number_field[0], phone_number_field[1])

    def get_ssn_field(self):
        return self.driver.find_element(ssn_field[0], ssn_field[1])

    def get_username_field(self):
        return self.driver.find_element(username_field[0], username_field[1])

    def get_password_field(self):
        return self.driver.find_element(password_field[0], password_field[1])

    def get_password_confirmation_field(self):
        return self.driver.find_element(password_confirmation_field[0], password_confirmation_field[1])

    def get_register_button(self):
        return self.driver.find_element(register_button[0], register_button[1])

    def get_registration_subtitle(self):
        return self.driver.find_element(registration_subtitle[0], registration_subtitle[1])
