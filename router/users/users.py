from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get("/users/health")
def users_health_check():
    return {"status": "OK"}

# endpoints for users can go here. 