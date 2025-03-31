from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from backend.app.services.roo.roo_core import handle_action

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Heimdal webhook is running"}