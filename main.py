from fastapi.testclient import TestClient  # Correct import for FastAPI
from main import app

client = TestClient(app)

def test_read_data():
    response = client.get("/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_data_by_guid():
    valid_guid = "12345"  # Replace with a valid GUID from your `data.json`
    response = client.get(f"/{valid_guid}")
    assert response.status_code == 200
    assert response.json()["guid"] == valid_guid

def test_read_data_by_invalid_guid():
    response = client.get("/invalid-guid")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"
