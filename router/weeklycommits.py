from fastapi import APIRouter, HTTPException, status
import datetime
from datetime import timedelta

from github import Github

router = APIRouter()

github = Github()

# return total number of commits in the past week
@router.get("/weeklycommits")
def return_weekly_commits(repo_name : str):
    repository = github.get_repo(repo_name)
    # find exact date 7 days before today and return number of commits since then
    today = datetime.datetime.now()
    last_week = today - timedelta(days=7) 

    commits=repository.get_commits(since=last_week)

    return {"Commits in the last week":commits.totalCount}

