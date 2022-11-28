from fastapi import APIRouter, HTTPException, status

from github import Github

router = APIRouter()

github = Github()

@router.get("/issues")
def get_repo_info(user_name : str):
    user = github.get_user(user_name)

    issue_list = {}
    for issue in user.get_issues:
        currentIssue = {
            "Name": issue.name,
            "State": issue.state,
            "Description": issue.description,
            "Date created": issue.created_at,
            "Date closed": issue.closed_at
        }
        issue_list[issue.name] = currentIssue
        
    return issue_list
