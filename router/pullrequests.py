from fastapi import APIRouter, HTTPException, status

from github import Github

router = APIRouter()

g = Github()


@router.get("/pulls")

def get_pulls(pulls: str):

    pull_requests = g.get_pulls(pulls)

    list_of_pulls = {}
   
    for pulls in pull_requests.get_pulls():
        pulls = {
            "Pull title": pulls.title,
            "Pull Number": pulls.number,
            "State of pull request": pulls.state,
            "Locked": pulls.locked,
        }
        list_of_pulls[pulls.title] = pulls

    return list_of_pulls
