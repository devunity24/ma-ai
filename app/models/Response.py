import json_repair
import re


class Response:
    def __init__(self, raw_response, llm, model, prompt):
        """
        Initialize Response object.

        Parameters:
            raw_response (object): Raw response object from the LLM.
            llm (str): Type of language model ('openai' or 'gemini').
            model (str): Model name.

        Raises:
            Exception: If llm is not 'openai' or 'gemini'.
        """
        self.raw_response = raw_response
        self.llm = llm
        self.model = model
        self.promptText = prompt
        
    def prompt(self):
        return self.promptText

    def text(self):
        """
        Extract and return text from raw response.

        Returns:
            str: Extracted text.

        Raises:
            Exception: If llm is neither 'openai' nor 'gemini'.
        """
        if self.llm == "openai":
            try:
                return self.raw_response.choices[0].text.strip()
            except Exception as ex:
                return self.raw_response["choices"][0]["message"]["content"]
        elif self.llm == "gemini":
            return self.raw_response.text
        elif self.llm == "bedrock_llama":
            return self.raw_response.strip()
        elif self.llm == "azure_openai":
            return self.raw_response
        else:
            raise Exception(f'Unknown LLM {self.llm}')

    def json(self):
        """
        Extract and repair JSON data from the response text.

        Returns:
            dict: Extracted and repaired JSON data.
        """
        text = self.text()
        json_part = re.search(r"^'(.+?)'$", text, re.DOTALL)
        if json_part:
            text = json_part.group(1)
        json_part = re.search(r'^"(.+?)"$', text, re.DOTALL)
        if json_part:
            text = json_part.group(1)
        json_part = re.search(r'```json\n(.+?)\n```', text, re.DOTALL)
        if json_part:
            text = json_part.group(1)
        else:
            json_part = re.search(r'```\n(.+?)\n```', text, re.DOTALL)
            if json_part:
                text = json_part.group(1)
        return json_repair.loads(text)
    
    def python(self):
        """
        Extract and repair JSON data from the response text.

        Returns:
            dict: Extracted and repaired JSON data.
        """
        text = self.text()
        python_code = re.search(r'```python\n(.+?)\n```', text, re.DOTALL)
        if python_code:
            text = python_code.group(1)
        else:
            python_code = re.search(r'```\n(.+?)\n```', text, re.DOTALL)
            if python_code:
                text = python_code.group(1)
        print(text)
        return text

    def mongo(self):
        """
        Extract and repair mongo data from the response text.

        Returns:
            dict: Extracted and repaired JSON data.
        """
        text = self.text()
        if '```mongodb' in text:
            json_part = re.search(r'```mongodb\n(.+?)\n```', text, re.DOTALL)
            if json_part:
                return json_part.group(1)
        elif '```javascript' in text:
            json_part = re.search(r'```javascript\n(.+?)\n```', text, re.DOTALL)
            if json_part:
                return json_part.group(1)

        return text

    def sql(self):
        """
        Extract and repair sql from the response text.

        Returns:
            dict: Extracted and repaired sql.
        """
        text = self.text()
        if '```sql' in text:
            json_part = re.search(r'```sql\n(.+?)\n```', text, re.DOTALL)
            if json_part:
                return json_part.group(1)
        return text

    def list(self):
        """
        Extract and return a list from the response text.

        Returns:
            list: Extracted list.
        """
        text = self.text()
        pattern = re.compile(r'^\d+\.?\s*')
        return [re.sub(pattern, '', line) for line in text.split('\n') if line.strip()]
    
    def getLLM(self):
        """
        Return LLM used to generate the response.

        Returns:
            str: llm.
        """
        return self.llm