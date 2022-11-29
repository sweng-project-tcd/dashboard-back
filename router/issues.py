from fastapi import APIRouter, HTTPException, status
from github import Github

router = APIRouter()
github = Github()

@router.get("/issues")
def get_repo_issues(repo_name : str):
    repository = github.get_repo(repo_name)

    issue_list = {}
    for issue in repository.get_issues():
        currentIssue = {
            "Assignee": issue.assignee.assignee,
            "Id": issue.id,
            "Commit Id": issue.commit_id,
            "Event": issue.event,
            "Date created": issue.created_at,
        }
        issue_list[issue.assignee.assignee] = currentIssue
        
    return issue_list
