from fastapi import APIRouter, HTTPException, status

from github import Github

router = APIRouter()

g = Github()


@router.get("/repositories")
def get_repository(username: str):
    user = g.get_user(username)

    repo_list = {}
    # iterates through all repos of the entered user,
    # creates a dictionary containing contents, then appends it to repo list dictionary
    for repo in user.get_repos():
        resp = {
            "Name": repo.full_name,
            "Description": repo.description,
            "Date Created": repo.created_at,
            "Date of last push": repo.pushed_at
        }
        repo_list[repo.full_name] = resp

    return repo_list
