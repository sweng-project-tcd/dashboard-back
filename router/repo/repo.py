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
    try:
        repository = github.get_repo(repo_name)
    except:
        raise HTTPException(status_code=404, detail="Repository not found")

    contributor_list = repository.get_stats_contributors()
    

    contributors_info = {}

  
    counter = 0
    for contributor in reversed(contributor_list):
        if counter == 6:
            break
        weekly_contribution = contributor.weeks
        contributors_info[contributor.author.name] = weekly_contribution[-1].c
        counter = counter + 1



    return contributors_info





# return total number of commits so for in the week (commits since the most recent monday)
@router.get("/repo/totalweeklycommits")
def return_weekly_commits(repo_name : str):
    try:
        repository = github.get_repo(repo_name)
    except:
        raise HTTPException(status_code=404, detail="Repository not found")

    today = datetime.datetime.now()
    most_recent_monday = today - timedelta(days=today.weekday())
    commits=repository.get_commits(since=most_recent_monday)

    return {
        "Commits in the last week":commits.totalCount,
        "Commits since": str(most_recent_monday.date())
    }



# return percentage increase for commits in the past week
@router.get("/repo/commitsincrease")
def calculate_commits_increase(repo_name:str):
    
    #find commits this week
    today = datetime.datetime.now()
    most_recent_monday = today - timedelta(days=today.weekday())
    last_weeks_monday = most_recent_monday - timedelta(days=7)

    try:
        repository = github.get_repo(repo_name)
    except:
        raise HTTPException(status_code=404, detail="Repository not found")

    this_week = repository.get_commits(since=most_recent_monday)
    commits_this_week = this_week.totalCount

    #find commits last week
    last_week = repository.get_commits(since=last_weeks_monday, until=most_recent_monday)
    commits_last_week = last_week.totalCount

    #find percentage increase
    percentage = ""
    if commits_last_week == 0:
        commits_this_week * 100
        percentage = str(commits_this_week) + "%"
    else:
        difference = commits_this_week - commits_last_week
        difference = difference / commits_last_week
        difference = round(difference*100, 1)
        percentage = str(difference) + "%"
    

    return{
        "Increase in commits in the past week": percentage,
        "Last week's date":str(last_weeks_monday.date())
    }

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