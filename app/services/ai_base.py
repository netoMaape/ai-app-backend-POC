from abc import ABC, abstractmethod

class BaseAIService(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Takes a prompt and returns a generated string."""
        pass