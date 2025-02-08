import allure
import pytest

from workflows.db_flows import DBFlows
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures("init_web_driver")
@pytest.mark.usefixtures("init_db_connection")
class TestWebDB:
    @allure.title("Login to Parabank via DB")
    @allure.description("This test verifies login using a database record")
    def test_verify_login_db(self):
        DBFlows.login_via_db_flow()
        actual = WebFlows.save_account_overview_title()
        WebFlows.log_out_flow()
        WebFlows.verify_title("Accounts Overview", actual)
