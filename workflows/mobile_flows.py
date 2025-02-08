import allure
import utilities.manage_pages as page
from extensions.mobile_actions import MobileActions
from extensions.verifications import Verifications


class MobileFlows:
    @staticmethod
    @allure.step("Add a new task")
    def add_task_flow(name):
        MobileActions.update_text(page.mobile_main.get_task_field(), name)
        MobileActions.click(page.mobile_main.get_add_task_button())

    @staticmethod
    @allure.step("Verify task exists")
    def verify_task_exists_flow(name):
        task_texts = [child.text for child in page.mobile_main.get_todo_list_task_names()]
        Verifications.verify_text_in_list(name, task_texts)

    @staticmethod
    @allure.step("Delete a task")
    def delete_task_flow(name):
        MobileActions.click(page.mobile_main.get_delete_button(name))

    @staticmethod
    @allure.step("Verify task does not exist")
    def verify_task_does_not_exist_flow(name):
        task_texts = [child.text for child in page.mobile_main.get_todo_list_task_names()]
        Verifications.verify_text_not_in_list(name, task_texts)

    @staticmethod
    @allure.step("Verify fill out field tooltip is displayed")
    def verify_fill_out_field_tooltip_displayed_flow():
        Verifications.is_displayed(page.mobile_main.get_fill_out_field_tooltip())

    @staticmethod
    @allure.step("Mark a task as completed")
    def mark_task_as_completed_flow(name):
        MobileActions.click(page.mobile_main.get_toggle_button(name))

    @staticmethod
    @allure.step("Display completed tasks")
    def display_completed_tasks_flow():
        MobileActions.click(page.mobile_main.get_completed_button())

    @staticmethod
    @allure.step("Display all tasks")
    def display_all_tasks_flow():
        MobileActions.click(page.mobile_main.get_all_button())

    @staticmethod
    @allure.step("Clear all tasks")
    def clear_all_tasks_flow():
        MobileActions.click(page.mobile_main.get_clear_all_button())

    @staticmethod
    @allure.step("Verify the todo list is empty")
    def verify_todo_list_is_empty_flow():
        Verifications.verify_equals(len(page.mobile_main.get_todo_list_children()), 0)
