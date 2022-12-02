from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_empty_pullrequests():
    response = client.get("/v1/pullrequests")
    assert response.status_code == 404
