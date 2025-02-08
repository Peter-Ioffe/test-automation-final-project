from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

transfer_amount_field = (By.ID, "amount")
to_account_selector = (By.ID, "toAccountId")
transfer_button = (By.XPATH, "//input[@value='Transfer']")
transfer_result_title = (By.XPATH, "//div[@id='showResult']/h1")


class TransferFundsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_transfer_amount_field(self):
        return self.driver.find_element(transfer_amount_field[0], transfer_amount_field[1])

    def get_to_account_selector(self):
        dropdown_element = self.driver.find_element(to_account_selector[0], to_account_selector[1])
        return Select(dropdown_element)

    def get_transfer_button(self):
        return self.driver.find_element(transfer_button[0], transfer_button[1])

    def get_transfer_result_title(self):
        return self.driver.find_element(transfer_result_title[0], transfer_result_title[1])
