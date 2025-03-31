from fastapi import FastAPI
from backend.app.api.api import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Heimdal webhook is running"}