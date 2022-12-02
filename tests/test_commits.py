from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_empty_commits():
    response = client.get("/v1/commits")
    assert response.status_code == 422


def test_commits():
    res = client.get(
        "/v1/commits?username=neilshevlin&start_date=2021-01-01&end_date=2021-01-31")
    assert res.status_code == 200
    assert res.json() == {"username": "neilshevlin",
                          "start_date": "2021-01-01", "end_date": "2021-01-31"}
