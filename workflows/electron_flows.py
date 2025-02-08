import allure
from selenium.webdriver.common.keys import Keys

import utilities.manage_pages as page
from extensions.ui_actions import UiActions


class ElectronFlows:
    @staticmethod
    @allure.step("Add a new task")
    def add_new_task_flow(task_name):
        UiActions.update_text(page.electron_task.get_create(), task_name)
        UiActions.update_text(page.electron_task.get_create(), Keys.RETURN)

    @staticmethod
    @allure.step("Get the number of tasks")
    def get_number_of_tasks_flow():
        return len(page.electron_task.get_tasks())

    @staticmethod
    @allure.step("Check a task as completed")
    def check_task_as_completed_flow(task_number):
        UiActions.mouse_hover_tooltip(page.electron_task.get_complete_checkboxes()[task_number - 1])

    @staticmethod
    @allure.step("Verify task is completed")
    def verify_task_is_completed_flow(task_number):
        label = page.electron_task.get_text_labels()[task_number - 1]
        if "completed_bHv-Q" in label.get_attribute("class"):
            return True
        else:
            return False

    @staticmethod
    @allure.step("Check all tasks as completed")
    def check_all_tasks_as_completed_flow():
        UiActions.mouse_hover_tooltip(page.electron_task.get_toggle_all_button())

    @staticmethod
    @allure.step("Verify all tasks are completed")
    def verify_all_tasks_are_completed_flow():
        labels = page.electron_task.get_text_labels()
        for label in labels:
            if "completed_bHv-Q" not in label.get_attribute("class"):
                return False
        return True

    @staticmethod
    @allure.step("Remove all tasks from the list")
    def remove_all_tasks_flow():
        for i in range(ElectronFlows.get_number_of_tasks_flow()):
            UiActions.wait_1_sec()
            UiActions.mouse_hover_tooltip(page.electron_task.get_delete_buttons()[0])
