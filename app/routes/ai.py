from fastapi import APIRouter

from app.services.GeneralAIService import GeneralAIService

router = APIRouter()

@router.get('/ai/temprun')
def temprun():
    aiService = GeneralAIService.getInstance("anthropic:claude-3-5-haiku-latest","")
    response = aiService.query("Who are you?")
    return {"response": response}