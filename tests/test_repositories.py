from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_empty_repositories():
    response = client.get("/v1/repositories")
    assert response.status_code == 422


def test_nonexisting_repositories():
    response = client.get("/v1/repositories?username=test")
    assert response.status_code == 404


def test_repositories_health_check():
    res = client.get("/v1/repo/health")
    assert res.status_code == 200
    assert res.json() == {"status": "OK"}
