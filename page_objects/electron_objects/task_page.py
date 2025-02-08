from selenium.webdriver.common.by import By

create = (By.CSS_SELECTOR, "input[placeholder='Create a task']")
tasks = (By.CLASS_NAME, "view_2Ow90")
delete_buttons = (By.XPATH, "//div[@class='view_2Ow90']/*[name()='svg']")
complete_checkboxes = (By.XPATH, "//div[@class='view_2Ow90']/label/*[name()='svg']")
text_labels = (By.XPATH, "//div[@class='textWrapper_X9gil']/label")
toggle_all_button = (By.XPATH, "//div[@class='allCompletedIconWrapper_2rCqr']/*[name()='svg']")


class TaskPage:
    def __init__(self, driver):
        self.driver = driver

    def get_create(self):
        return self.driver.find_element(create[0], create[1])

    def get_tasks(self):
        return self.driver.find_elements(tasks[0], tasks[1])

    def get_delete_buttons(self):
        return self.driver.find_elements(delete_buttons[0], delete_buttons[1])

    def get_complete_checkboxes(self):
        return self.driver.find_elements(complete_checkboxes[0], complete_checkboxes[1])

    def get_text_labels(self):
        return self.driver.find_elements(text_labels[0], text_labels[1])

    def get_toggle_all_button(self):
        return self.driver.find_element(toggle_all_button[0], toggle_all_button[1])
