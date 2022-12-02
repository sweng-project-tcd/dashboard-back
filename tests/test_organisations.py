from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

def test_users_health_check():
    res = client.get("v1/users/health")
    assert res.status_code == 200
    assert res.json() == {"status": "OK"}