import json

from app.models.Prompt import Prompt
from app.models.Response import Response
from app.util.Utility import Utility
from app.util.Logger import Logger
from app.models.OpenAI import OpenAI
from langchain.chat_models import ChatOpenAI


class DeepAI:

    __openai_key = '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'

    @staticmethod
    def generateWithMultiplePrompt(systemPrompt: Prompt, userPrompt: Prompt, assistantPrompt: Prompt = Prompt(), childId: str = 'master', actionMsg: str = '',
                                   temperature: float = 0, max_tokens: int = 10000) -> Response:
        """
        Generates text using a specified OpenAI model, given a prompt.

        Args:
            systemPrompt (Prompt): The system prompt to provide to the AI model.
            userprompt (Prompt): The user prompt to provide to the AI model.


        Returns:
            Response: The generated text response.
        """
        llm = "openai"

        if Utility.isStringNonEmpty(actionMsg):
            Logger.info(
                f'Prompt to {actionMsg} : "{userPrompt.get_prompt()}" by {llm}', childId)
            
        model = ChatOpenAI(temperature=0, model_name='gpt-4o', openai_api_key=DeepAI.__openai_key);

        llm_instance = OpenAI(DeepAI.__openai_key, model=model, temperature=temperature, max_tokens=max_tokens, top_p=0.9, frequency_penalty=0, presence_penalty=2, stop=[])
        return llm_instance.generateWithMultiplePrompt(systemPrompt=systemPrompt, userPrompt=userPrompt, assistantPrompt=assistantPrompt)

