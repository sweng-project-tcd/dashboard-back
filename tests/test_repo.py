from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_commits_increase():
    response = client.get("v1/repo/commitsincrease")
    assert response.status_code == 422

    response = client.get("v1/repo/commitsincrase?repo_name=testtest")
    assert response.status_code == 404


def test_total_weekly_commits():
    response = client.get("v1/repo/totalweeklycommits")
    assert response.status_code == 422

    #response = client.get("v1/repo/totalweeklycommits?repo_name=testtest")
    #assert response.status_code == 404

def test_contributors():
    response = client.get("v1/repo/contributors")
    assert response.status_code == 422

    #response = client.get("v1/repo/contributors?repo_name=testtest")
    #assert response.status_code == 404
