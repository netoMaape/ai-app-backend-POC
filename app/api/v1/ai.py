from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.deps import get_current_user
from app.db.models import User
from app.services.mock_ai import MockAIService
from app.core.config import settings

router = APIRouter()

# Factory function to get the right AI service
def get_ai_service():
    if settings.AI_PROVIDER == "mock":
        return MockAIService()
    # if settings.AI_PROVIDER == "openai": return OpenAIService(...)
    return MockAIService()

ai_provider = get_ai_service()

class SummarizeRequest(BaseModel):
    text: str

class SummarizeResponse(BaseModel):
    summary: str

@router.post("/summarize", response_model=SummarizeResponse)
def summarize_text(
    request: SummarizeRequest, 
    current_user: User = Depends(get_current_user)
):
    """
    Summarize the provided text using the configured AI provider.
    """
    # In a real app, you'd pass the prompt to the AI service here
    prompt = f"Summarize this text: {request.text}"
    result = ai_provider.generate_response(prompt)
    return {"summary": result}