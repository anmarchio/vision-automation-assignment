import unittest
import json
from unittest.mock import patch

from starlette.testclient import TestClient

from endpoints.api_endpoint import app


class TestApiEndpoint(unittest.TestCase):

    def setUp(self):
        # Set up test client
        self.client = TestClient(
            app,
            base_url="localhost",
            raise_server_exceptions=True,
            root_path="",
            backend="asyncio",
            backend_options=None,
            cookies=None,
            headers=None,
            follow_redirects=True,
            client=("testclient", 50000),
        )

    @patch("endpoints.api_endpoint.fi_confidence")  # Mock any internal processing function
    def test_post_request(self, mock_process_image):
        # Define a successful response
        mock_process_image.return_value = {"status": "success", "result": "processed"}

        # Sample payload
        payload = {
            "fi_confidence": "base64_encoded_image_string_here"
        }

        response = self.client.post(self.endpoint, data=json.dumps(payload))

        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.json)
        self.assertEqual(response.json["status"], "success")

    def test_get_request(self):
        # Missing payload test
        response = self.client.post(self.endpoint, data=json.dumps({}), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json)
        self.assertEqual(response.json["error"], "No serial id found")


if __name__ == "__main__":
    unittest.main()
