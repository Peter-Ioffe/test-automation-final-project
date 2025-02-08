import allure

from extensions.ui_actions import UiActions
import utilities.manage_pages as page


class DesktopFlows:
    @staticmethod
    @allure.step("Calculate an equation")
    def calculate_flow(equation):
        for i in equation:
            DesktopFlows.calculator_click(i)
        UiActions.click(page.standard_calculator.get_equals())

    @staticmethod
    def calculator_click(value):
        if value == "0":
            UiActions.click(page.standard_calculator.get_zero())
        elif value == "1":
            UiActions.click(page.standard_calculator.get_one())
        elif value == "2":
            UiActions.click(page.standard_calculator.get_two())
        elif value == "3":
            UiActions.click(page.standard_calculator.get_three())
        elif value == "4":
            UiActions.click(page.standard_calculator.get_four())
        elif value == "5":
            UiActions.click(page.standard_calculator.get_five())
        elif value == "6":
            UiActions.click(page.standard_calculator.get_six())
        elif value == "7":
            UiActions.click(page.standard_calculator.get_seven())
        elif value == "8":
            UiActions.click(page.standard_calculator.get_eight())
        elif value == "9":
            UiActions.click(page.standard_calculator.get_nine())
        elif value == "+":
            UiActions.click(page.standard_calculator.get_plus())
        elif value == "-":
            UiActions.click(page.standard_calculator.get_minus())
        elif value == "*":
            UiActions.click(page.standard_calculator.get_mult())
        elif value == "/":
            UiActions.click(page.standard_calculator.get_divide())
        elif value == ".":
            UiActions.click(page.standard_calculator.get_decimal_point())
        elif value == "(":
            UiActions.click(page.scientific_calculator.get_left_parenthesis())
        elif value == ")":
            UiActions.click(page.scientific_calculator.get_right_parenthesis())
        elif value == "e":
            UiActions.click(page.scientific_calculator.get_euler_number())
        else:
            raise Exception("Invalid Input: " + value)

    @staticmethod
    @allure.step("Get the calculated result")
    def get_result_flow():
        result = page.standard_calculator.get_result().text.replace("Display is", "").strip()
        return result

    @staticmethod
    @allure.step("Store and add to memory")
    def memory_add_flow(value):
        for i in value:
            DesktopFlows.calculator_click(i)
        UiActions.click(page.standard_calculator.get_memory_add())

    @staticmethod
    @allure.step("Recall from memory")
    def memory_recall_flow():
        UiActions.click(page.standard_calculator.get_memory_recall())

    @staticmethod
    @allure.step("Select a calculator mode")
    def select_calculator_mode_flow(mode):
        current_header = page.standard_calculator.get_header().text
        if current_header.lower() != mode:
            UiActions.click(page.navigation_page.get_open_navigation())
            if mode == "standard":
                UiActions.click(page.navigation_page.get_standard_calculator())
            elif mode == "scientific":
                UiActions.click(page.navigation_page.get_scientific_calculator())
            elif mode == "graphing":
                UiActions.click(page.navigation_page.get_graphing_calculator())
            elif mode == "programmer":
                UiActions.click(page.navigation_page.get_programmer_calculator())
            elif mode == "date calculation":
                UiActions.click(page.navigation_page.get_date_calculation_calculator())
            else:
                raise Exception("Unknown mode: " + mode)

    @staticmethod
    @allure.step("Calculate sine")
    def calculate_sine_flow():
        UiActions.click(page.scientific_calculator.get_trigonometry())
        UiActions.click(page.scientific_calculator.get_sine())

    @staticmethod
    @allure.step("Calculate natural logarithm")
    def calculate_natural_logarithm_flow(value):
        for i in value:
            DesktopFlows.calculator_click(i)
        UiActions.click(page.scientific_calculator.get_natural_log())

    @staticmethod
    @allure.step("Clear the calculator display")
    def clear_flow():
        clear_buttons = page.standard_calculator.get_clear()
        if clear_buttons and clear_buttons[0].is_displayed():
            UiActions.click(clear_buttons[0])
            return
        clear_entry_buttons = page.standard_calculator.get_clear_entry()
        if clear_entry_buttons and clear_entry_buttons[0].is_displayed():
            UiActions.click(clear_entry_buttons[0])
            clear_buttons = page.standard_calculator.get_clear()
            if clear_buttons and clear_buttons[0].is_displayed():
                UiActions.click(clear_buttons[0])
        else:
            print("Neither C nor CE was available for clicking.")
