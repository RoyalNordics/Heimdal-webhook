from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

import os

app = FastAPI()

port = int(os.environ.get("PORT", 8000))

@app.post("/webhook")
async def webhook_endpoint(request: Request):
    try:
        data = await request.json()
        action = data.get("action")
        filename = data.get("filename")
        content = data.get("content")
        assistant_id = data.get("assistant_id")

        from webhook.roo import roo_core
        response = roo_core.handle_action(action, filename, content, assistant_id)
        return JSONResponse(content=response)


    except Exception as e:
        response_data = {
            "status": "error",
            "message": str(e)
        }
        return JSONResponse(content=response_data)

@app.get("/test_openai")
async def test_openai_endpoint():
    try:
        import openai
        from webhook import config
        openai.api_key = config.OPENAI_API_KEY
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or any other suitable engine
            prompt="This is a test prompt. Please respond with a short message.",
            max_tokens=50
        )
        response_data = {
            "status": "success",
            "message": response.choices[0].text.strip()
        }
        return JSONResponse(content=response_data)
    except Exception as e:
        response_data = {
            "status": "error",
            "message": str(e)
        }
        return JSONResponse(content=response_data)