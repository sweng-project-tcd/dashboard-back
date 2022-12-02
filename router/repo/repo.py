from fastapi import APIRouter, HTTPException, status
import datetime
from datetime import timedelta
from github import Github

router = APIRouter()

github = Github()

@router.get("/repo/health")
def repo_health_check():
    return {"status": "OK"}

# return each contributor with their number of commits in the last week
@router.get("/repo/contributors")
def return_individual_contributions(repo_name:str):
    repository = github.get_repo(repo_name)



# return total number of commits in the past week
@router.get("/repo/totalweeklycommits")
def return_weekly_commits(repo_name : str):
    repository = github.get_repo(repo_name)
    today = datetime.datetime.now()
    last_week = today - timedelta(days=7) 

    commits=repository.get_commits(since=last_week)

    return {"Commits in the last week":commits.totalCount}



# return percentage increase for commits in the past week
@router.get("/repo/commitsincrease")
def calculate_commits_increase(repo_name:str):
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

    percentage = ""
    if commits_last_week == 0:
        commits_this_week * 100
        percentage = commits_this_week + "%"
    
    difference = commits_this_week - commits_last_week
    difference = int(difference / commits_last_week)
    difference = difference*100
    percentage = str(difference) + "%"
    

    return{"Increase in commits in the past week": percentage}

# @router.get("/issues")
# def get_repo_issues(repo_name : str):
#     repository = github.get_repo(repo_name)

#     issue_list = {}
#     for issue in repository.get_issues():
#         currentIssue = {
#             "Assignee": issue.assignee.assignee,
#             "Id": issue.id,
#             "Commit Id": issue.commit_id,
#             "Event": issue.event,
#             "Date created": issue.created_at,
#         }
#         issue_list[issue.assignee.assignee] = currentIssue
        
#     return issue_list