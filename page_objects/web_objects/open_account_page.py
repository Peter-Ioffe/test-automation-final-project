from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

account_type_selector = (By.ID, "type")
open_new_account_button = (By.XPATH, "//input[@value='Open New Account']")
account_result_title = (By.XPATH, "//div[@id='openAccountResult']/h1")


class OpenAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def get_account_type_selector(self):
        dropdown_element = self.driver.find_element(account_type_selector[0], account_type_selector[1])
        return Select(dropdown_element)

    def get_open_new_account_button(self):
        return self.driver.find_element(open_new_account_button[0], open_new_account_button[1])

    def get_account_result_title(self):
        return self.driver.find_element(account_result_title[0], account_result_title[1])
