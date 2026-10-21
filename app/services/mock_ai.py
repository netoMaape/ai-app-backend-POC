from app.services.ai_base import BaseAIService

class MockAIService(BaseAIService):
    def generate_response(self, prompt: str) -> str:
        text1 = "📝 **Mock Summary: "
        text2 = "** This is a simulated AI summary of your text. In a real app, you would use OpenAI or Gemini here. Prompt length chars: " + ({len(prompt)} )
        return text1 + text2