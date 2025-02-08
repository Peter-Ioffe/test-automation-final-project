from selenium.webdriver.common.by import By

open_navigation = (By.NAME, "Open Navigation")
standard_calculator = (By.NAME, "Standard Calculator")
scientific_calculator = (By.NAME, "Scientific Calculator")
graphing_calculator = (By.NAME, "Graphing Calculator")
programmer_calculator = (By.NAME, "Programmer Calculator")
date_calculation_calculator = (By.NAME, "Date calculation Calculator")


class NavigationPage:
    def __init__(self, driver):
        self.driver = driver

    def get_open_navigation(self):
        return self.driver.find_element(open_navigation[0], open_navigation[1])

    def get_standard_calculator(self):
        return self.driver.find_element(standard_calculator[0], standard_calculator[1])

    def get_scientific_calculator(self):
        return self.driver.find_element(scientific_calculator[0], scientific_calculator[1])

    def get_graphing_calculator(self):
        return self.driver.find_element(graphing_calculator[0], graphing_calculator[1])

    def get_programmer_calculator(self):
        return self.driver.find_element(programmer_calculator[0], programmer_calculator[1])

    def get_date_calculation_calculator(self):
        return self.driver.find_element(date_calculation_calculator[0], date_calculation_calculator[1])
