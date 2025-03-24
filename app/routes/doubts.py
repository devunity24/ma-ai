from fastapi import APIRouter, Request
from app.logics.Doubts import Doubts
from fastapi.responses import JSONResponse
from app.util.Logger import Logger
import traceback

router = APIRouter()


doubts = Doubts()

@router.get("/resolve-doubt")
async def resolve_doubt(request: Request, childId: str= 'master'):
    
    request_body = await request.json()
    try:
        answer = doubts.get_answer(
            board=request_body.get("board"),
            class_=request_body.get("grade"),
            subject=request_body.get("subject"),
            chapter=request_body.get("chapter"),
            lesson=request_body.get("lesson"),
            question=request_body.get("question"),
            previous_questions=request_body.get("previous_questions"),
            child_id=childId
        )
        
        return get_empty_json() if answer is None else JSONResponse(content=answer)
    except Exception as e:
        Logger.error(message=str(e), childId=childId)
        Logger.error(message=traceback.format_exc(), childId=childId)
        error_message = {
            "developerMessage": str(e),
            "userMessage": "Oops, this wasn't supposed to happen !!!",
            "errorCode": 50001
        }
        return JSONResponse(content=error_message, status_code=500)
    
def get_empty_json():
        return JSONResponse(content={}, status_code=200)