from fastapi import FastAPI
from router.test import router as sample_router
from router.repositories import router as repo_router
from router.contributors import router as contributor_router
from router.issues import router as issue_router
from router.pullrequests import router as pull_request_router
from router.commits import router as commit_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:3000',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sample_router, prefix="/v1", tags=["test"])

# router for repositories 
app.include_router(repo_router, prefix="/v1", tags=["repositories"])

#router for contributors
app.include_router(contributor_router, prefix="/v1", tags=["contributors"])

#router for issues
app.include_router(issue_router, prefix="/v1", tags=["issues"])

#router for pull requests
app.include_router(pull_request_router, prefix="/v1", tags=["pullrequests"])

#router for commits
app.include_router(commit_router, prefix="/v1", tags=["commits"])
