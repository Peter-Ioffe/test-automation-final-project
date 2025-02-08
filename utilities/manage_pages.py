import test_cases.conftest
from page_objects.desktop_objects.navigation_page import NavigationPage
from page_objects.desktop_objects.scientific_page import ScientificPage
from page_objects.desktop_objects.standard_page import StandardPage
from page_objects.electron_objects.task_page import TaskPage
from page_objects.mobile_objects.main_page import MainPage
from page_objects.web_objects.account_overview_page import AccountOverviewPage
from page_objects.web_objects.loan_page import LoanPage
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.registration_page import RegistrationPage
from page_objects.web_objects.open_account_page import OpenAccountPage
from page_objects.web_objects.transfer_funds_page import TransferFundsPage

# Web Objects
web_login = None
web_account_overview = None
web_registration = None
web_loan = None
web_open_account = None
web_transfer_funds = None

# Mobile Objects
mobile_main = None

# Electron Objects
electron_task = None

# Desktop Objects
standard_calculator = None
navigation_page = None
scientific_calculator = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()["web_login"] = LoginPage(test_cases.conftest.driver)
        globals()["web_account_overview"] = AccountOverviewPage(test_cases.conftest.driver)
        globals()["web_registration"] = RegistrationPage(test_cases.conftest.driver)
        globals()["web_loan"] = LoanPage(test_cases.conftest.driver)
        globals()["web_open_account"] = OpenAccountPage(test_cases.conftest.driver)
        globals()["web_transfer_funds"] = TransferFundsPage(test_cases.conftest.driver)

    @staticmethod
    def init_mobile_pages():
        globals()["mobile_main"] = MainPage(test_cases.conftest.driver)

    @staticmethod
    def init_electron_pages():
        globals()["electron_task"] = TaskPage(test_cases.conftest.driver)

    @staticmethod
    def init_desktop_pages():
        globals()["standard_calculator"] = StandardPage(test_cases.conftest.driver)
        globals()["navigation_page"] = NavigationPage(test_cases.conftest.driver)
        globals()["scientific_calculator"] = ScientificPage(test_cases.conftest.driver)
