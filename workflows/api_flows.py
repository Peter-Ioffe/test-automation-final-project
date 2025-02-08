import allure

from extensions.api_actions import APIActions
from utilities.common_ops import get_data

url = get_data("UrlApi")


class APIFlows:
    @staticmethod
    @allure.step("Get all posts")
    def get_all_posts_flow():
        response = APIActions.get(url + "posts")
        response_json = response.json()
        return response_json

    @staticmethod
    @allure.step("Get a post")
    def get_a_post_flow(post_id):
        response = APIActions.get(url + "posts/" + str(post_id))
        response_json = response.json()
        return response_json

    @staticmethod
    @allure.step("Get value from JSON server API")
    def get_value_from_api_flow(nodes):
        response = APIActions.get(url + "posts")
        return APIActions.extract_value_from_response(response, nodes)

    @staticmethod
    @allure.step("Create a new post")
    def create_post_flow(user_id, post_id, title, body):
        payload = {"userId": user_id, "id": post_id, "title": title, "body": body}
        status_code = APIActions.post(url + "posts", payload)
        return status_code

    @staticmethod
    @allure.step("Update a post")
    def update_post_flow(user_id, post_id, title, body):
        payload = {"userId": user_id, "id": post_id, "title": title, "body": body}
        status_code = APIActions.put(url + "posts/" + str(post_id), payload)
        return status_code

    @staticmethod
    @allure.step("Delete a post")
    def delete_post_flow(post_id):
        status_code = APIActions.delete(url + "posts/" + str(post_id))
        return status_code
