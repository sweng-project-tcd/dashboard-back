from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_empty_commits():
    response = client.get("/v1/commits")
    assert response.status_code == 422