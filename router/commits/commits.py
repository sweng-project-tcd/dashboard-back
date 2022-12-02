from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get("/commits/health")
def commits_health_check():
    return {"status": "OK"}

# This method is meant to return the number of commits from a user in a given date range
# @router.get("/commits")
# def get_commits(username : str, start_date : str, end_date : str):

#     response = req.get(f"https://api.github.com/search/commits?q=author:{username}&order-desc", headers={"Accept": "application/vnd.github.cloak-preview"})#This gets the public commits for the user

#     items = response.json()["items"]
#     dates = []
#     for el in items:
#         dates.append(el["commit"]["author"]["date"])
#     # sort dates in ascending order
#     dates.sort(key=lambda date: date)
#     if response.status_code == 200:
#         print(response.json())
#         return {"username": username, "start_date": start_date, "end_date": end_date, "total_commits": response.json()["total_count"]}
#     else:
#         raise HTTPException(status_code=404, detail="User not found")