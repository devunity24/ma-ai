from app.models.Prompt import Prompt
from app.models.Response import Response


class LLM:
    """
    Abstract base class representing a Large Language Model.
    """

    def __init__(self, api_key: str=None, model: str=None, temperature: float=0, max_tokens: int=1000, top_p: float=0.9, frequency_penalty: int=0,
                 presence_penalty: int = 2, stop: list = []):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.stop = stop

    def generate(self, prompt: Prompt) -> Response:
        """
        Generates text based on the provided prompt.

        Args:
          prompt (str): The text prompt for the LLM.

        Returns:
          str: The generated text response.
        """
        raise NotImplementedError(
            "This method must be implemented in subclasses.")
        
    def generateWithMultiplePrompt(self, systemPrompt: Prompt, userPrompt: Prompt, assistantPrompt: Prompt) -> Response:
        """
        Generates text based on the provided prompt.

        Args:
          systemPrompt (str): The text system prompt for the LLM.
          userPrompt (str): The text user prompt for the LLM.
          assistantPrompt (str): The text assistant prompt for the LLM.

        Returns:
          str: The generated text response.
        """
        raise NotImplementedError(
            "This method must be implemented in subclasses.")
