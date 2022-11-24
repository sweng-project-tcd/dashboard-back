from fastapi import FastAPI

from router.test import router as sample_router
from router.repositories import router as repo_router
from router.contributors import router as contributor_router

app = FastAPI()

app.include_router(sample_router, prefix="/test", tags=["test"])

# router for repositories 
app.include_router(repo_router, prefix="/repositories", tags=["repositories"])

#router for contributors
app.include_router(contributor_router, prefix="/contributors", tags=["contributors"])




