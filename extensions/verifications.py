import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:
    @staticmethod
    @allure.step("Verify equality")
    def verify_equals(actual, expected):
        assert actual == expected, "Verification of equality failed. Actual: " + str(
            actual) + " is not equal to Expected " + str(expected)

    @staticmethod
    @allure.step("Verify element is displayed")
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), "Verification of display failed. Elem " + elem.text + " is not displayed."

    @staticmethod
    @allure.step("Verify text is present in list")
    def verify_text_in_list(text_to_find: str, text_list: list):
        has_specific_text = any(text_to_find in item for item in text_list)
        assert has_specific_text, f"'{text_to_find}' task not found in the list."

    @staticmethod
    @allure.step("Verify text is not present in list")
    def verify_text_not_in_list(text_to_find: str, text_list: list):
        has_specific_text = any(text_to_find in item for item in text_list)
        assert not has_specific_text, f"'{text_to_find}' task is found in the list, but it should not exist."

    @staticmethod
    @allure.step("Soft verification (assert) of elements using smart assertions")
    def soft_assert(elements):
        for i in range(len(elements)):
            soft_assert(elements[i].is_displayed())
        verify_expectations()

    @staticmethod
    @allure.step("Soft verification (assert) of elements using soft display implementation")
    def soft_displayed(elements):
        failed_elements = []
        for i in range(len(elements)):
            if not elements[i].is_displayed():
                failed_elements.insert(len(failed_elements), elements[i].get_attribute("id"))
        if len(failed_elements) > 0:
            for failed_elem in failed_elements:
                print("Soft display failed on element: " + str(failed_elem))
            raise AssertionError("Soft display failed.")
