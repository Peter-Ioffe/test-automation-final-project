from selenium.webdriver.common.by import By

trigonometry = (By.NAME, "Trigonometry")
sine = (By.NAME, "Sine")
right_parenthesis = (By.NAME, "Right parenthesis")
left_parenthesis = (By.NAME, "Left parenthesis")
euler_number = (By.NAME, "Euler's number")
natural_log = (By.NAME, "Natural log")


class ScientificPage:
    def __init__(self, driver):
        self.driver = driver

    def get_trigonometry(self):
        return self.driver.find_element(trigonometry[0], trigonometry[1])

    def get_sine(self):
        return self.driver.find_element(sine[0], sine[1])

    def get_right_parenthesis(self):
        return self.driver.find_element(right_parenthesis[0], right_parenthesis[1])

    def get_left_parenthesis(self):
        return self.driver.find_element(left_parenthesis[0], left_parenthesis[1])

    def get_euler_number(self):
        return self.driver.find_element(euler_number[0], euler_number[1])

    def get_natural_log(self):
        return self.driver.find_element(natural_log[0], natural_log[1])
