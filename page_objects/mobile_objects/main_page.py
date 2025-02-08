from selenium.webdriver.common.by import By

task_field = (By.ID, "todo-input")
add_task_button = (By.XPATH, "//*[@text='Add Task']")
all_button = (By.ID, "filter-all")
active_button = (By.ID, "filter-active")
completed_button = (By.ID, "filter-completed")
clear_completed_button = (By.ID, "clear-completed")
clear_all_button = (By.ID, "clear-all")
todo_list = (By.ID, "todo-list")
todo_list_children = (By.ID, "todo-list")
todo_list_task_names = (By.XPATH, "(//*[@id='todo-list']/*/*[@class='android.widget.TextView' and ./parent::*["
                                  "@class='android.view.View']])")
delete_button = (By.XPATH, "//*[@text='Delete' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)["
                           "@text='{TASK_NAME}']]]")
toggle_button = (By.XPATH, "//*[@text='Toggle' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)["
                           "@text='{TASK_NAME}']]]")
fill_out_field_tooltip = (By.XPATH, "//*[@text='Please fill out this field. ']")


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def get_task_field(self):
        return self.driver.find_element(task_field[0], task_field[1])

    def get_add_task_button(self):
        return self.driver.find_element(add_task_button[0], add_task_button[1])

    def get_all_button(self):
        return self.driver.find_element(all_button[0], all_button[1])

    def get_active_button(self):
        return self.driver.find_element(active_button[0], active_button[1])

    def get_completed_button(self):
        return self.driver.find_element(completed_button[0], completed_button[1])

    def get_clear_completed_button(self):
        return self.driver.find_element(clear_completed_button[0], clear_completed_button[1])

    def get_clear_all_button(self):
        return self.driver.find_element(clear_all_button[0], clear_all_button[1])

    def get_todo_list(self):
        return self.driver.find_element(todo_list[0], todo_list[1])

    def get_todo_list_children(self):
        return self.driver.find_elements(todo_list_children[0], todo_list_children[1])

    def get_todo_list_task_names(self):
        return self.driver.find_elements(todo_list_task_names[0], todo_list_task_names[1])

    def get_delete_button(self, task_name):
        dynamic_xpath = delete_button[1].replace("{TASK_NAME}", task_name)
        return self.driver.find_element(delete_button[0], dynamic_xpath)

    def get_toggle_button(self, task_name):
        dynamic_xpath = toggle_button[1].replace("{TASK_NAME}", task_name)
        return self.driver.find_element(toggle_button[0], dynamic_xpath)

    def get_fill_out_field_tooltip(self):
        return self.driver.find_element(fill_out_field_tooltip[0], fill_out_field_tooltip[1])
