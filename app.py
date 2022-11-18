from fastapi import FastAPI

from router.test import router as sample_router
from router.repositories import router as repo_router
app = FastAPI()

app.include_router(sample_router, prefix="/test", tags=["test"])

# router for repositories 
app.include_router(repo_router, prefix="/repositories", tags=["repositories"])




