import allure
import pytest

from utilities.common_ops import get_data
from workflows import web_flows
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures("init_web_driver")
class TestWeb:
    @allure.title("Verify registration")
    @allure.description("This test verifies a successful registration in Parabank")
    def test_verify_registration(self):
        WebFlows.register_flow(get_data("FirstName"), get_data("LastName"), get_data("Address"), get_data("City"),
                               get_data("State"), get_data("ZipCode"), get_data("PhoneNumber"), get_data("SSN"),
                               get_data("Username"), get_data("Password"))
        actual = WebFlows.save_registration_result_message()
        WebFlows.log_out_flow()
        WebFlows.verify_title("Your account was created successfully. You are now logged in.", actual)

    @allure.title("Verify login")
    @allure.description("This test verifies a successful login to Parabank")
    def test_verify_login(self):
        WebFlows.login_flow(get_data("Username"), get_data("Password"))
        actual = WebFlows.save_account_overview_title()
        WebFlows.log_out_flow()
        WebFlows.verify_title("Accounts Overview", actual)

    @allure.title("Verify invalid login")
    @allure.description("This test verifies an invalid login to Parabank")
    def test_verify_invalid_login(self):
        WebFlows.login_flow("blabla", get_data("Password"))
        WebFlows.verify_login_error("The username and password could not be verified.")

    @allure.title("Verify requesting a loan")
    @allure.description("This test verifies a successful loan request from Parabank")
    @pytest.mark.parametrize("loan_amount, down_payment", web_flows.testdata)
    def test_request_loan(self, loan_amount, down_payment):
        WebFlows.login_flow(get_data("Username"), get_data("Password"))
        WebFlows.request_loan_flow(loan_amount, down_payment)
        actual = WebFlows.save_loan_request_status()
        WebFlows.log_out_flow()
        WebFlows.verify_title("Approved", actual)

    @allure.title("Verify opening a new account")
    @allure.description("This test verifies successful creation of a new account in Parabank")
    def test_open_new_account(self):
        WebFlows.login_flow(get_data("Username"), get_data("Password"))
        WebFlows.open_new_account_flow("SAVINGS")
        actual = WebFlows.save_new_account_creation_result()
        WebFlows.log_out_flow()
        WebFlows.verify_title("Account Opened!", actual)

    # Pre-condition: The user has at least two accounts with sufficient balance in the source account.
    @allure.title("Verify fund transfer")
    @allure.description("This test verifies a successful fund transfer between two accounts")
    def test_verify_transfer_funds(self):
        WebFlows.login_flow(get_data("Username"), get_data("Password"))
        WebFlows.transfer_funds_flow("5")
        actual = WebFlows.save_fund_transfer_status()
        WebFlows.log_out_flow()
        WebFlows.verify_title("Transfer Complete!", actual)

    # @allure.title("Visual testing")
    # @allure.description("This test verifies loan request page visually")
    # @pytest.mark.skipif(get_data("ExecuteApplitools").lower() == "no", reason="test for demo purposes")
    # def test_verify_visual(self):
    #     conf.eyes.open(self.driver, "Parabank", "Parabank Account overview page")
    #     WebFlows.login_flow(get_data("Username"), get_data("Password"))
    #     conf.eyes.check_window("Account overview page")

    # Demo test for smart assertions
    # def test_verify_registration_form_fields(self):
    #     WebFlows.verify_registration_form_smart_assertions()
