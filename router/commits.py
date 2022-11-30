from fastapi import APIRouter, HTTPException, status

router = APIRouter()


# This method is meant to return the number of commits from a user in a given date range
@router.get("/commits")
def get_commits(username : str, start_date : str, end_date : str):
    return {"repository_name": "test"}