import allure

from extensions.db_actions import DBActions
from workflows.web_flows import WebFlows


class DBFlows:
    @staticmethod
    @allure.step('Login via DB')
    def login_via_db_flow():
        columns = ['Name', 'Password']
        result = DBActions.get_query_result(columns, "Users", "ID", "1")
        WebFlows.login_flow(result[0][0], result[0][1])
