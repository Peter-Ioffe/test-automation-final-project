import allure

import page_objects.web_objects.account_overview_page
import page_objects.web_objects.registration_page
import page_objects.web_objects.login_page
import page_objects.web_objects.loan_page
import page_objects.web_objects.open_account_page
import page_objects.web_objects.transfer_funds_page
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, For, get_data, read_csv


class WebFlows:
    @staticmethod
    @allure.step("Login to Parabank flow")
    def login_flow(user: str, password: str):
        UiActions.update_text(page.web_login.get_username_field(), user)
        UiActions.update_text(page.web_login.get_password_field(), password)
        UiActions.click(page.web_login.get_log_in_button())

    @staticmethod
    @allure.step("Saving Account overview title")
    def save_account_overview_title():
        wait(For.ELEMENT_EXISTS, page_objects.web_objects.account_overview_page.account_overview_title)
        actual = page.web_account_overview.get_account_overview_title().text
        return actual

    @staticmethod
    @allure.step("Verifying expected title/message was displayed")
    def verify_title(expected: str, actual):
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step("New user registration flow")
    def register_flow(first_name, last_name, address, city, state, zip_code, phone_number, ssn, username, password):
        UiActions.click(page.web_login.get_register_link())
        UiActions.update_text(page.web_registration.get_first_name_field(), first_name)
        UiActions.update_text(page.web_registration.get_last_name_field(), last_name)
        UiActions.update_text(page.web_registration.get_address_field(), address)
        UiActions.update_text(page.web_registration.get_city_field(), city)
        UiActions.update_text(page.web_registration.get_state_field(), state)
        UiActions.update_text(page.web_registration.get_zip_code_field(), zip_code)
        UiActions.update_text(page.web_registration.get_phone_number_field(), phone_number)
        UiActions.update_text(page.web_registration.get_ssn_field(), ssn)
        UiActions.update_text(page.web_registration.get_username_field(), username)
        UiActions.update_text(page.web_registration.get_password_field(), password)
        UiActions.update_text(page.web_registration.get_password_confirmation_field(), password)
        UiActions.click(page.web_registration.get_register_button())

    @staticmethod
    @allure.step("Saving registration result message")
    def save_registration_result_message():
        wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.registration_page.registration_subtitle)
        actual = page.web_registration.get_registration_subtitle().text
        return actual

    @staticmethod
    @allure.step("Verifying that login error message is displayed")
    def verify_login_error(expected: str):
        wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.login_page.error_message)
        actual = page.web_login.get_error_message().text
        Verifications.verify_equals(actual, expected)

    @staticmethod
    @allure.step("Loan request flow")
    def request_loan_flow(loan_amount: str, down_payment: str):
        UiActions.click(page.web_login.get_request_loan_link())
        UiActions.update_text(page.web_loan.get_loan_amount_field(), loan_amount)
        UiActions.update_text(page.web_loan.get_down_payment_field(), down_payment)
        UiActions.click(page.web_loan.get_apply_button())

    @staticmethod
    @allure.step("Saving loan request status")
    def save_loan_request_status():
        wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.loan_page.loan_status_field)
        actual = page.web_loan.get_loan_status_field().text
        return actual

    @staticmethod
    @allure.step("New account creation flow")
    def open_new_account_flow(account_type: str):
        UiActions.click(page.web_login.get_open_new_account_link())
        account_type_dropdown = page.web_open_account.get_account_type_selector()
        account_type_dropdown.select_by_visible_text(account_type)
        UiActions.wait_1_sec()
        UiActions.click(page.web_open_account.get_open_new_account_button())

    @staticmethod
    @allure.step("Saving new account creation result")
    def save_new_account_creation_result():
        wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.open_account_page.account_result_title)
        actual = page.web_open_account.get_account_result_title().text
        return actual

    @staticmethod
    @allure.step("Transfer funds flow")
    def transfer_funds_flow(transfer_amount: str):
        UiActions.click(page.web_login.get_transfer_funds_link())
        UiActions.update_text(page.web_transfer_funds.get_transfer_amount_field(), transfer_amount)
        to_account_dropdown = page.web_transfer_funds.get_to_account_selector()
        to_account_dropdown.select_by_index(1)
        UiActions.click(page.web_transfer_funds.get_transfer_button())

    @staticmethod
    @allure.step("Saving fund transfer status")
    def save_fund_transfer_status():
        wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.transfer_funds_page.transfer_result_title)
        actual = page.web_transfer_funds.get_transfer_result_title().text
        return actual

    @staticmethod
    @allure.step("Logging out flow")
    def log_out_flow():
        UiActions.click(page.web_login.get_log_out_link())
        Verifications.is_displayed(page.web_login.get_register_link())

    @staticmethod
    @allure.step("Verifying display of registration form elements using smart assertions")
    def verify_registration_form_smart_assertions():
        UiActions.click(page.web_login.get_register_link())
        elements = [page.web_registration.get_first_name_field(),
                    page.web_registration.get_last_name_field(),
                    page.web_registration.get_address_field(),
                    page.web_registration.get_city_field(),
                    page.web_registration.get_state_field(),
                    page.web_registration.get_zip_code_field(),
                    page.web_registration.get_phone_number_field(),
                    page.web_registration.get_ssn_field(),
                    page.web_registration.get_username_field(),
                    page.web_registration.get_password_field(),
                    page.web_registration.get_password_confirmation_field()]
        Verifications.soft_assert(elements)

    @staticmethod
    @allure.step("Verifying display of registration form elements using soft display implementation")
    def verify_registration_form_soft_display():
        UiActions.click(page.web_login.get_register_link())
        elements = [page.web_registration.get_first_name_field(),
                    page.web_registration.get_last_name_field(),
                    page.web_registration.get_address_field(),
                    page.web_registration.get_city_field(),
                    page.web_registration.get_state_field(),
                    page.web_registration.get_zip_code_field(),
                    page.web_registration.get_phone_number_field(),
                    page.web_registration.get_ssn_field(),
                    page.web_registration.get_username_field(),
                    page.web_registration.get_password_field(),
                    page.web_registration.get_password_confirmation_field()]
        Verifications.soft_displayed(elements)


data = read_csv(get_data("CsvLocation"))
testdata = [
    (data[0][0], data[0][1]),
    (data[1][0], data[1][1]),
    (data[2][0], data[2][1]),
    ]
