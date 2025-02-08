from selenium.webdriver.common.by import By

loan_amount_field = (By.ID, "amount")
down_payment_field = (By.ID, "downPayment")
apply_button = (By.XPATH, "//input[@value='Apply Now']")
loan_status_field = (By.ID, "loanStatus")


class LoanPage:
    def __init__(self, driver):
        self.driver = driver

    def get_loan_amount_field(self):
        return self.driver.find_element(loan_amount_field[0], loan_amount_field[1])

    def get_down_payment_field(self):
        return self.driver.find_element(down_payment_field[0], down_payment_field[1])

    def get_apply_button(self):
        return self.driver.find_element(apply_button[0], apply_button[1])

    def get_loan_status_field(self):
        return self.driver.find_element(loan_status_field[0], loan_status_field[1])
