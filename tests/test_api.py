

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_investors():
    response = client.get("/api/v1/investors/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "investor_name" in response.json()[0]

def test_read_investor_byId():
    response = client.get("/api/v1/investors/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_read_asset_classes():
    response = client.get("/api/v1/asset-classes")
    assert response.status_code == 200
    assert isinstance(response.json()["asset_classes"], list)
