from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_empty_repositories():
    response = client.get("/v1/repositories")
    assert response.status_code == 422


def test_nonexisting_repositories():
    response = client.get("/v1/repos")
    assert response.status_code == 404
