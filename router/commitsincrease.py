from fastapi import APIRouter, HTTPException, status
import datetime
from datetime import timedelta
from github import Github

router = APIRouter()

github = Github()

@router.get("/commitsincrease")
def calculate_commits_increase(repo_name:str):
    try:
        today = datetime.datetime.now()
        most_recent_monday = today - timedelta(days=today.weekday())
        last_weeks_monday = most_recent_monday - timedelta(days=7)
        #find commits this week
    
        repository = github.get_repo(repo_name)

        this_week = repository.get_commits(since=most_recent_monday)
        commits_this_week = this_week.totalCount

        #find commits last week
        last_week = repository.get_commits(since=last_weeks_monday, until=most_recent_monday)
        commits_last_week = last_week.totalCount

        #find percentage increase
        return_message = {}

        percentage = ""
        if commits_last_week == 0:
            commits_this_week * 100
            percentage = commits_this_week + "%"
        
        difference = commits_this_week - commits_last_week
        difference = difference / commits_last_week
        

        return{"test": last_weeks_monday}
    except:
        return{"repo":"not found"}