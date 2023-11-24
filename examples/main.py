import unittest
from main import Client, ParamsValueType  # You need to provide this module

class TestClient(unittest.TestCase):

    def test_access_token(self):
        app_id = ""
        app_secret = ""

        dataopen_client = Client(app_id, app_secret)
        dataopen_client.get_token()

        self.assertIsNotNone(dataopen_client.is_authenticated())
        print("Output is_authenticated: ", dataopen_client.is_authenticated())

    def test_request_get(self):
        app_id = "cli_4184c7da025ad1"
        app_secret = ""

        dataopen_client = Client(app_id, app_secret)

        headers = {}

        params: dict[str, ParamsValueType] = {
            "app": 46,
            "page_size": 1,
            "page": 1,
        }

        body = {}

        res = dataopen_client.request("/dataopen/open-apis/xxx/openapi/v1/open/flight-list", "GET", headers, params, body)
        print("\n\nOutput: ", res)

    def test_request_post(self):
        app_id = ""
        app_secret = ""

        dataopen_client = Client(app_id, app_secret)

        headers = {}

        params = {}

        body: dict[str, any] = {
            "uid_list": ["1111111110000"],
        }

        res = dataopen_client.request(
            "/dataopen/open-apis/xxx/openapi/v1/open/flight/version/6290880/add-test-user",
            "POST",
            headers,
            params,
            body,
        )

        # Output results
        print("\n\nOutput: ", res)

    def test_request_material_post(self):
        app_id = ""
        app_secret = ""

        dataopen_client = Client(app_id, app_secret, "https://analytics.volcengineapi.com")

        headers = {}

        params = {}

        body: dict[str, any] = {
            "name": "ccnnodetest",
            "title": "测试title",
            "type": "component",
            "description": "测试description3",
            "frameworkType": "react",
        }

        res = dataopen_client.request(
             "/material/openapi/v1/material",
            "PUT",
            headers,
            params,
            body,
        )

        # Output results
        print("\n\nOutput: ", res)

if __name__ == "__main__":
    unittest.main()