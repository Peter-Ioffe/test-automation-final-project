import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

import test_cases.conftest


class UiActions:
    @staticmethod
    @allure.step("Clicking on element")
    def click(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step("Updating text")
    def update_text(elem: WebElement, value: str):
        elem.send_keys(value)

    @staticmethod
    @allure.step("Hovering over tooltip/one element")
    def mouse_hover_tooltip(elem: WebElement):
        ActionChains(test_cases.conftest.driver).move_to_element(elem).click().perform()

    @staticmethod
    @allure.step("Hovering over two elements")
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        test_cases.conftest.action.move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step("Right-clicking an element")
    def right_click(elem: WebElement):
        test_cases.conftest.action.context_click(elem).perform()

    @staticmethod
    @allure.step("Dragging and dropping an element")
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        test_cases.conftest.action.drag_and_drop(elem1, elem2).perform()

    @staticmethod
    @allure.step("Clearing text from an element")
    def clear(elem: WebElement):
        elem.clear()

    @staticmethod
    @allure.step("Waiting 1 second")
    def wait_1_sec():
        time.sleep(1)
