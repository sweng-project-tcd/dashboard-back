from fastapi import FastAPI


from router.commits.commits import router as commits_router
from router.organisations.organisations import router as organisations_router
from router.users.users import router as users_router
from router.repo.repo import router as repositories_router

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

app.include_router(repositories_router, prefix="/v1", tags=["repositories"])

#router for contributors
app.include_router(commits_router, prefix="/v1", tags=["commits"])

#router for issues
app.include_router(organisations_router, prefix="/v1", tags=["organisations"])

#router for pull requests
app.include_router(users_router, prefix="/v1", tags=["users"])

