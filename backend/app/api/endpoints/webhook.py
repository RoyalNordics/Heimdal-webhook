from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from backend.app.services.roo.roo_core import handle_action

router = APIRouter()

@router.post("/")
async def receive_webhook(request: Request):
    try:
        payload = await request.json()
        result = await handle_action(payload)
        return JSONResponse(content={"success": True, "result": result}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"success": False, "error": str(e)}, status_code=500)