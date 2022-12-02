from fastapi import APIRouter, HTTPException, status, Query
from datetime import timedelta
from datetime import datetime
from github import Github
import random

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
    
# return total number of commits in the past week
@router.get("/repo/commits")
def return_weekly_commits(repo_name : str, start : datetime = Query(None), end : datetime = Query(None)):

    # the url that the user should be passing in is something like ?start=2022-01-01&end=2022-01-31

    # parses the dates passed in to a datetime object. This is the format that the github api uses
    start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end, "%Y-%m-%d")

    repository = github.get_repo(repo_name)
    commits=repository.get_commits(since=start_date, until=end_date)

    return {"commits":commits.totalCount}




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

@router.get("/dummy/repo/commits")
def dummy_repo_commits(start: str, end: str):
    # generate a random number of commits based on the start and end dates
    # this is just a dummy method for testing purposes

    # get the number fo days between the start and end dates
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    delta = end_date - start_date
    print(delta)

    # generate a random number of commits based on the number of days
    num_commits = random.randint(0, delta.days)

    authors = ['John', 'Jane', 'Bob', 'Alice', 'Joe', 'Mary', 'Tom', 'Sally', 'Sue', 'Sam']

    last_num_commits = random.randint(0, delta.days)

    #  get thepercentage change in commits
    percentage = 0
    if last_num_commits == 0:
        num_commits * 100
        percentage = num_commits
    else:
        difference = num_commits - last_num_commits
        difference = difference / last_num_commits
        difference = round(difference*100, 1)
        percentage = difference

    print(percentage)

    return {
        "num_commits": num_commits,
        "percent_change": percentage,
        "authors": authors,
        "start_date": start,
        "end_date": end,
    }

@router.get("/dummy/repo/bugs")
def dummy_repo_commits(start: str, end: str):
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    delta = end_date - start_date

    monthly_bug_rate = []

    random.seed(0)

    x = 0

    for i in range(delta.days):
        # values have to be positive
        dx = random.gauss(0, 1)
        if dx < 0:
            dx = 0
        x += dx
        monthly_bug_rate.append(int(x))

    print(monthly_bug_rate)



    
    return {
        "num_bugs": len(monthly_bug_rate),
        "num_bugs_prev": 10,
        "percent_change": 20,
        "start_date": start,
        "end_date": end,
        "values": monthly_bug_rate,

    }

