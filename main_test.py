import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestApp(unittest.TestCase):
    def test_read_data(self):
        """
        Test that all data is retrieved successfully.
        """
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_read_data_by_guid(self):
        """
        Test fetching an item by a valid GUID.
        """
        valid_guid = "12345"  # Replace with a GUID from your data.json
        response = client.get(f"/{valid_guid}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["guid"], valid_guid)

    def test_read_data_by_invalid_guid(self):
        """
        Test fetching an item with an invalid GUID.
        """
        response = client.get("/invalid-guid")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "Item not found")


if __name__ == "__main__":
    unittest.main()
