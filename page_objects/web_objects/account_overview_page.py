from selenium.webdriver.common.by import By

account_overview_title = (By.XPATH, "//div[@id='showOverview']/h1[@class='title']")


class AccountOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_account_overview_title(self):
        return self.driver.find_element(account_overview_title[0], account_overview_title[1])
