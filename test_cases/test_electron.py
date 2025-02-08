import allure
import pytest

from extensions.verifications import Verifications
from workflows.electron_flows import ElectronFlows


@pytest.mark.usefixtures("init_electron_driver")
class TestElectron:
    @allure.title("Verify adding a task")
    @allure.description("This test verifies adding a task to the todo list")
    def test_verify_adding_task(self):
        ElectronFlows.add_new_task_flow("Learn Python")
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(), 1)

    @allure.title("Verify adding multiple tasks")
    @allure.description("This test verifies adding multiple tasks to the todo list")
    def test_verify_adding_multiple_tasks(self):
        ElectronFlows.add_new_task_flow("Learn Java")
        ElectronFlows.add_new_task_flow("Learn C#")
        ElectronFlows.add_new_task_flow("Learn JavaScript")
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(), 3)

    @allure.title("Verify checking task as completed")
    @allure.description("This test verifies checking task as completed")
    def test_verify_checking_task_as_completed(self):
        ElectronFlows.add_new_task_flow("Learn Python")
        ElectronFlows.check_task_as_completed_flow(1)
        Verifications.verify_equals(ElectronFlows.verify_task_is_completed_flow(1), True)

    @allure.title("Verify checking all tasks as completed")
    @allure.description("This test verifies checking all tasks as completed")
    def test_verify_checking_all_tasks_as_completed(self):
        ElectronFlows.add_new_task_flow("Learn Java")
        ElectronFlows.add_new_task_flow("Learn C#")
        ElectronFlows.add_new_task_flow("Learn JavaScript")
        ElectronFlows.check_all_tasks_as_completed_flow()
        Verifications.verify_equals(ElectronFlows.verify_all_tasks_are_completed_flow(), True)

    def teardown_method(self):
        ElectronFlows.remove_all_tasks_flow()
