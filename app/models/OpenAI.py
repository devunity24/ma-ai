import openai
from app.models.LLM import LLM
from app.models.Prompt import Prompt
from app.models.Response import Response


class OpenAI(LLM):
    """
    Subclass representing the OpenAI GPT LLM.
    """

    def __init__(self, api_key: str, model: str="gpt-3.5-turbo-instruct", temperature: float=0, max_tokens: int=1000, top_p: float=0.9, frequency_penalty: int=0,
                           presence_penalty: int=2, stop: list=[]):
        max_tokens = 4000 if (max_tokens) > 4000 else max_tokens
        model = model if model else "gpt-3.5-turbo-instruct"
        super().__init__(api_key, model, temperature, max_tokens, top_p, frequency_penalty, presence_penalty, stop)
        openai.api_key = api_key

    def generate(self, prompt: Prompt) -> Response:
        return self.generateWithMultiplePrompt(Prompt(), prompt, None)

    def generateWithMultiplePrompt(self, systemPrompt: Prompt, userPrompt: Prompt, assistantPrompt: Prompt) -> Response:
        messages = []
        if assistantPrompt is not None and len(assistantPrompt.get_prompt()) > 0:
            messages = [
                {"role": "system", "content": systemPrompt.get_prompt()},
                {"role": "user", "content": userPrompt.get_prompt()},
                {"role": "assistant", "content": assistantPrompt.get_prompt()}
            ]
        else:    
            messages = [
                {"role": "system", "content": systemPrompt.get_prompt()},
                {"role": "user", "content": userPrompt.get_prompt()}
            ]
            
        response = openai.ChatCompletion.create(
            model='gpt-4o',
            messages=messages,
            temperature=self.temperature
        )
        
        return Response(response, llm="openai", model='gpt-4o', prompt=userPrompt.get_prompt())
