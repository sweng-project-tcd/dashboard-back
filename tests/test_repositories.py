from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

def test_repositories_health_check():
    res = client.get("/v1/repo/health")
    assert res.status_code == 200
    assert res.json() == {"status": "OK"}