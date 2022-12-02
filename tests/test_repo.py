from fastapi.testclient import TestClient
import datetime
from datetime import timedelta
import json



from app import app

client = TestClient(app)

most_recent_monday = datetime.datetime.now() - timedelta(days=datetime.datetime.now().weekday())
last_weeks_monday = most_recent_monday - timedelta(days=7)
last_weeks_monday = last_weeks_monday.date()



def test_commits_increase():
    response = client.get("v1/repo/commitsincrease")
    assert response.status_code == 422

    response = client.get("v1/repo/commitsincrease?repo_name=StevenCataluna/pico-apps")
    assert response.status_code == 200

    # check if the date of last week's monday matches up
    data = response.json()
    assert data["Last week's date"] == str(last_weeks_monday)

    # check error code for invalid repo
    response = client.get("v1/repo/commitsincrease?repo_name=test")
    assert response.status_code == 404


def test_total_weekly_commits():
    response = client.get("v1/repo/totalweeklycommits")
    assert response.status_code == 422

    # test invalid repo
    response = client.get("v1/repo/totalweeklycommits?repo_name=testtest")
    assert response.status_code == 404

    # test if returned date is correct
    response = client.get("v1/repo/totalweeklycommits?repo_name=strapi/strapi")
    assert response.status_code == 200
    data = response.json()
    assert data["Commits since"] == str(most_recent_monday.date())

def test_contributors():
    response = client.get("v1/repo/contributors")
    assert response.status_code == 422
    # test invalid repo
    response = client.get("v1/repo/contributors?repo_name=testtest")
    assert response.status_code == 404

    # check if returned values are all ints
    response = client.get("v1/repo/contributors?repo_name=strapi/strapi")
    assert response.status_code == 200
    data = response.json()
    values = data.values()
    assert all(isinstance(val, int) for val in values)
