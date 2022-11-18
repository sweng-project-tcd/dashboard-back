from fastapi import FastAPI

from router.test import router as sample_router
app = FastAPI()

app.include_router(test_router, prefix="/test", tags=["test"])






