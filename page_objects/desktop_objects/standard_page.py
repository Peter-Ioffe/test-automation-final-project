from selenium.webdriver.common.by import By

zero = (By.NAME, "Zero")
one = (By.NAME, "One")
two = (By.NAME, "Two")
three = (By.NAME, "Three")
four = (By.NAME, "Four")
five = (By.NAME, "Five")
six = (By.NAME, "Six")
seven = (By.NAME, "Seven")
eight = (By.NAME, "Eight")
nine = (By.NAME, "Nine")
plus = (By.NAME, "Plus")
minus = (By.NAME, "Minus")
mult = (By.NAME, "Multiply by")
divide = (By.NAME, "Divide by")
equals = (By.NAME, "Equals")
clear = (By.NAME, "Clear")
clear_entry = (By.NAME, "Clear entry")
result = (By.XPATH, "//*[@AutomationId='CalculatorResults']")
decimal_point = (By.NAME, "Decimal separator")
memory_add = (By.NAME, "Memory add")
memory_recall = (By.NAME, "Memory recall")
header = (By.XPATH, "//*[@AutomationId='Header']")


class StandardPage:
    def __init__(self, driver):
        self.driver = driver

    def get_zero(self):
        return self.driver.find_element(zero[0], zero[1])

    def get_one(self):
        return self.driver.find_element(one[0], one[1])

    def get_two(self):
        return self.driver.find_element(two[0], two[1])

    def get_three(self):
        return self.driver.find_element(three[0], three[1])

    def get_four(self):
        return self.driver.find_element(four[0], four[1])

    def get_five(self):
        return self.driver.find_element(five[0], five[1])

    def get_six(self):
        return self.driver.find_element(six[0], six[1])

    def get_seven(self):
        return self.driver.find_element(seven[0], seven[1])

    def get_eight(self):
        return self.driver.find_element(eight[0], eight[1])

    def get_nine(self):
        return self.driver.find_element(nine[0], nine[1])

    def get_plus(self):
        return self.driver.find_element(plus[0], plus[1])

    def get_minus(self):
        return self.driver.find_element(minus[0], minus[1])

    def get_mult(self):
        return self.driver.find_element(mult[0], mult[1])

    def get_divide(self):
        return self.driver.find_element(divide[0], divide[1])

    def get_equals(self):
        return self.driver.find_element(equals[0], equals[1])

    def get_clear(self):
        return self.driver.find_elements(clear[0], clear[1])

    def get_clear_entry(self):
        return self.driver.find_elements(clear_entry[0], clear_entry[1])

    def get_result(self):
        return self.driver.find_element(result[0], result[1])

    def get_decimal_point(self):
        return self.driver.find_element(decimal_point[0], decimal_point[1])

    def get_memory_add(self):
        return self.driver.find_element(memory_add[0], memory_add[1])

    def get_memory_recall(self):
        return self.driver.find_element(memory_recall[0], memory_recall[1])

    def get_header(self):
        return self.driver.find_element(header[0], header[1])
