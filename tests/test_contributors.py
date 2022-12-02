from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_empty_contributors():
    response = client.get("/v1/contributors")
    assert response.status_code == 422


def test_nonexisting_contributors():
    response = client.get("/v1/contributor")
    assert response.status_code == 404
