from selenium.webdriver.common.by import By

username_field = (By.NAME, "username")
password_field = (By.NAME, "password")
log_in_button = (By.XPATH, "//input[@value='Log In']")
register_link = (By.LINK_TEXT, "Register")
error_message = (By.CSS_SELECTOR, "p[class='error']")
request_loan_link = (By.LINK_TEXT, "Request Loan")
accounts_overview_link = (By.LINK_TEXT, "Account Overview")
open_new_account_link = (By.LINK_TEXT, "Open New Account")
transfer_funds_link = (By.LINK_TEXT, "Transfer Funds")
log_out_link = (By.LINK_TEXT, "Log Out")


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_username_field(self):
        return self.driver.find_element(username_field[0], username_field[1])

    def get_password_field(self):
        return self.driver.find_element(password_field[0], password_field[1])

    def get_log_in_button(self):
        return self.driver.find_element(log_in_button[0], log_in_button[1])

    def get_register_link(self):
        return self.driver.find_element(register_link[0], register_link[1])

    def get_request_loan_link(self):
        return self.driver.find_element(request_loan_link[0], request_loan_link[1])

    def get_error_message(self):
        return self.driver.find_element(error_message[0], error_message[1])

    def get_accounts_overview_link(self):
        return self.driver.find_element(accounts_overview_link[0], accounts_overview_link[1])

    def get_open_new_account_link(self):
        return self.driver.find_element(open_new_account_link[0], open_new_account_link[1])

    def get_transfer_funds_link(self):
        return self.driver.find_element(transfer_funds_link[0], transfer_funds_link[1])

    def get_log_out_link(self):
        return self.driver.find_element(log_out_link[0], log_out_link[1])
