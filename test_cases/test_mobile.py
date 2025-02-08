import allure
import pytest

from workflows.mobile_flows import MobileFlows


@pytest.mark.usefixtures("init_mobile_driver")
class TestMobile:
    @allure.title("Verify adding a task")
    @allure.description("This test verifies adding a task to the todo list")
    def test_verify_adding_task(self):
        MobileFlows.add_task_flow("Test task")
        MobileFlows.verify_task_exists_flow("Test task")

    @allure.title("Verify deleting a task")
    @allure.description("This test verifies deleting a task from the todo list")
    def test_verify_deleting_task(self):
        MobileFlows.add_task_flow("Test task 2")
        MobileFlows.delete_task_flow("Test task 2")
        MobileFlows.verify_task_does_not_exist_flow("Test task 2")

    @allure.title("Verify a task with no name cannot be created")
    @allure.description("This test verifies that a task without a name cannot be added to the todo list")
    def test_verify_cannot_create_task_without_name(self):
        MobileFlows.add_task_flow("")
        MobileFlows.verify_fill_out_field_tooltip_displayed_flow()

    @allure.title("Verify a task is marked as completed")
    @allure.description("This test verifies a task is marked as completed")
    def test_completing_task(self):
        MobileFlows.add_task_flow("Test task 3")
        MobileFlows.mark_task_as_completed_flow("Test task 3")
        MobileFlows.display_completed_tasks_flow()
        MobileFlows.verify_task_exists_flow("Test task 3")

    @allure.title("Verify clearing all tasks")
    @allure.description("This test verifies clearing all tasks from the todo list")
    def test_verify_clearing_all_tasks(self):
        MobileFlows.add_task_flow("Test task 4")
        MobileFlows.add_task_flow("Test task 5")
        MobileFlows.add_task_flow("Test task 6")
        MobileFlows.display_all_tasks_flow()
        MobileFlows.clear_all_tasks_flow()
        MobileFlows.verify_todo_list_is_empty_flow()
