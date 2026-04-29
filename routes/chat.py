from fastapi import APIRouter
from models.schema import ChatRequest,ChatResponse
from services.llm import process_chat
router=APIRouter()

@router.post("/chat" ,response_model=ChatResponse)
def chat(request:ChatRequest):
    response,history=process_chat(request.message)
    return {"response": response, "history": history}
@router.post("/reset")
def reset():
    reset_history()
    return {"message": "History cleared"}
