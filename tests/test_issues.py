from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_empty_issues():
    response = client.get("/v1/issues")
    assert response.status_code == 422


def test_nonexisting_issues():
    response = client.get("/v1/issue")
    assert response.status_code == 404
