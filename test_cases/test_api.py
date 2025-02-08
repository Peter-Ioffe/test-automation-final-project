import allure

from extensions.verifications import Verifications
from workflows.api_flows import APIFlows


class TestAPI:
    @allure.title("Create a post and verify the status code")
    @allure.description("This test creates a new post")
    def test_create_post_and_verify_status(self):
        actual_status_code = APIFlows.create_post_flow(11, 101, "test", "lorem ipsum")
        Verifications.verify_equals(actual_status_code, 201)

    @allure.title("Verify number of posts")
    @allure.description("This test verifies the number of posts")
    def test_verify_number_of_posts(self):
        actual_posts_number = len(APIFlows.get_all_posts_flow())
        Verifications.verify_equals(actual_posts_number, 101)

    @allure.title("Update a post and verify the status code")
    @allure.description("This test updates an existing post")
    def test_update_post_and_verify_status(self):
        actual_status_code = APIFlows.update_post_flow(11, 101, "test", "dolor sit amet")
        Verifications.verify_equals(actual_status_code, 200)

    @allure.title("Verify a post's body")
    @allure.description("This test verifies a post's body")
    def test_verify_post_body(self):
        actual_post_body = APIFlows.get_a_post_flow(101)["body"]
        Verifications.verify_equals(actual_post_body, "dolor sit amet")

    @allure.title("Delete a post and verify the status code")
    @allure.description("This test deletes a post")
    def test_delete_post(self):
        actual_status_code = APIFlows.delete_post_flow(101)
        Verifications.verify_equals(actual_status_code, 200)

    @allure.title("Delete a non-existent post and verify the status code")
    @allure.description("This test tries to delete a non-existent post")
    def test_delete_non_existent_post(self):
        actual_status_code = APIFlows.delete_post_flow(9999)
        Verifications.verify_equals(actual_status_code, 404)
