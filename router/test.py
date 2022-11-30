from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get("/test")
async def root():
    resp = {
        "message": "Test Router",
        "id": "1234",
        "github_repo": "https://github.com"
    }
    return resp
