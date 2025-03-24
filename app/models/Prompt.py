class Prompt:
    """
    A class for constructing prompts for OpenAI or Gemini models.
    """

    def __init__(self, initial_prompt=None):
        self._prompt = initial_prompt if initial_prompt else ""

    def append(self, text):
        """Adds text to the end of the prompt and returns itself."""
        self._prompt += text
        return self

    def append_if(self, condition, text):
        """Adds text to the end of the prompt and returns itself."""
        if condition == True:
            self._prompt += text
        return self

    def new_line(self):
        """Adds text to the end of the prompt and returns itself."""
        self._prompt += "\n"
        return self

    def prepend(self, text):
        """Prepends text to the beginning of the prompt and returns itself."""
        self._prompt = text + self._prompt
        return self

    def json(self):
        """Adds a prompt for generating an answer in JSON format and returns itself."""
        self.append(
            "Generate the following reponse in JSON format:\n")
        return self

    def get_prompt(self):
        """Returns the final prompt string."""
        return self._prompt
