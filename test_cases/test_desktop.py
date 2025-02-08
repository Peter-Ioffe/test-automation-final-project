import allure
import pytest

from extensions.verifications import Verifications
from workflows.desktop_flows import DesktopFlows


@pytest.mark.usefixtures("init_desktop_driver")
class TestDesktop:
    @allure.title("Addition of two integers")
    @allure.description("This test adds two integer numbers and verifies the result")
    def test_add_integers(self):
        DesktopFlows.select_calculator_mode_flow("standard")
        DesktopFlows.calculate_flow("2+7")
        Verifications.verify_equals(DesktopFlows.get_result_flow(), "9")

    @allure.title("Subtraction of two floats")
    @allure.description("This test subtracts one floating-point number from another and verifies the result")
    def test_subtract_floats(self):
        DesktopFlows.select_calculator_mode_flow("standard")
        DesktopFlows.calculate_flow("5.95-2.5")
        Verifications.verify_equals(DesktopFlows.get_result_flow(), "3.45")

    @allure.title("Basic arithmetic operations")
    @allure.description("This test uses chained basic arithmetic operations and verifies the result")
    def test_basic_arithmetic_operations(self):
        DesktopFlows.select_calculator_mode_flow("standard")
        DesktopFlows.calculate_flow("2*5+50/2-25")
        Verifications.verify_equals(DesktopFlows.get_result_flow(), "5")

    @allure.title("Division by zero")
    @allure.description("This test confirms error handling for division by zero")
    def test_divide_by_zero(self):
        DesktopFlows.select_calculator_mode_flow("standard")
        DesktopFlows.calculate_flow("10/0")
        Verifications.verify_equals(DesktopFlows.get_result_flow(), "Cannot divide by zero")

    @allure.title("Memory store and recall")
    @allure.description("This test validates memory store, addition and recall functionality")
    def test_memory_store_and_recall(self):
        DesktopFlows.select_calculator_mode_flow("standard")
        DesktopFlows.memory_add_flow("10")
        DesktopFlows.clear_flow()
        DesktopFlows.memory_add_flow("5")
        DesktopFlows.memory_recall_flow()
        Verifications.verify_equals(DesktopFlows.get_result_flow(), "15")

    @allure.title("Parentheses usage")
    @allure.description("This test uses parentheses in an expression and verifies the result")
    def test_parentheses_usage(self):
        DesktopFlows.select_calculator_mode_flow("scientific")
        DesktopFlows.calculate_flow("(2+3)*(4-1)")
        Verifications.verify_equals(DesktopFlows.get_result_flow(), "15")

    @allure.title("Sine calculation")
    @allure.description("This test calculates sine and verifies the result")
    def test_sine_calculation(self):
        DesktopFlows.select_calculator_mode_flow("scientific")
        DesktopFlows.calculate_flow("30")
        DesktopFlows.calculate_sine_flow()
        Verifications.verify_equals(DesktopFlows.get_result_flow(), "0.5")

    @allure.title("Natural logarithm calculation")
    @allure.description("This test calculates natural logarithm and verifies the result")
    def test_natural_logarithm_calculation(self):
        DesktopFlows.select_calculator_mode_flow("scientific")
        DesktopFlows.calculate_natural_logarithm_flow("e")
        Verifications.verify_equals(DesktopFlows.get_result_flow(), "1")

    def teardown_method(self):
        DesktopFlows.clear_flow()
