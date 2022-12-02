from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get("/organisations/health")
def organisations_health_check():
    return {"status": "OK"}

# endpoints for orgs can go here. 