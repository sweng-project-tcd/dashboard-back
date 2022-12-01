from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_null_repository():
    response = client.get("/v1/contributors")
    assert response.status_code == 422

def test_incorrect_repository():
    response = client.get("/v1/contributors?repo_name=test")

    assert response.status_code == 200
    assert response.json() == {"repository":"not found"}
