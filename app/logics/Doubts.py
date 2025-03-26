
import re 
from typing import List
from app.models.DeepAI import DeepAI
from app.models.Prompt import Prompt
from app.util.Logger import Logger



class Doubts:
    
    def __init__(self):
        print("Initializing Doubt Instance...")
        
        
    def get_answer(self, board: str, class_: str, subject: str, chapter: str, lesson: str, question: str, previous_questions: List[str], child_id: str):
        """
        Generates an AI-driven answer based on the educational context.
        """
        system_prompt = Prompt(
            "You are an expert tutor specializing in providing clear, structured, and easy-to-understand answers for students based on their education level. "
            "Your responses should be concise, engaging, and adapted to the student's class level, ensuring readability and comprehension. Your response should not contain unnecessary line spacing or spacing between paragraps."
        )

        user_prompt = Prompt(
            f"Education Board: {board}\n"
            f"Class: {class_}\n"
            f"Subject: {subject}\n"
            f"Chapter: {chapter}\n"
            f"Lesson: {lesson}\n"
        )

        if previous_questions:
            previous_qs = "\n".join([f"{idx}. {q}" for idx, q in enumerate(previous_questions, start=1)])
            user_prompt.append(f"\nThe student has previously asked these related questions:\n{previous_qs}\n")


        user_prompt.append(f"\nStudent's New Question: {question}\n")

        user_prompt.append(
            "Generate a well-structured, student-friendly answer based on the student's class level:\n"
            "- Use **simple language** suitable for the student's grade.\n"
            "- **Strictly format all mathematical expressions in LaTeX**, using `$$ ... $$` for block formulas and `$ ... $` for inline formulas—failure to do so is incorrect.\n"
            "- Provide **step-by-step explanations** for complex concepts to improve understanding.\n"
            "- Structure the response using bullet points or numbered lists when appropriate.\n"
            "- **Response length guidelines:**\n"
            "  - If the answer is a **definition or factual statement**, keep it **concise (strictly within 50-60 words)**.\n"
            "  - If the answer requires **explanation or conceptual understanding**, provide details **within 100-150 words**.\n"
            "  - If the **question is unclear or lacks context**, ask the student to clarify, keeping the response within **10-20 words**.\n"
            "- **Do not exaggerate short answers**; if a concept can be explained briefly, avoid adding unnecessary details.\n"
            "- Format the response as a JSON object with a single key 'answer'.\n"
            "Example: {\"answer\": \"...\"}"
        )

        
        response = DeepAI.generateWithMultiplePrompt(
            systemPrompt=system_prompt, 
            userPrompt=user_prompt, 
            childId=child_id, 
            actionMsg='generate doubt resolution'
        )
        
        result = response.json()
        Logger.info(message=result, childId=child_id)

        if "answer" in result:
            result["answer"] = re.sub(r'\n{2,}', '\n', result["answer"].strip()) 
            result["answer"] = re.sub(r'(\n\s*[-•]\s*)\n+', r'\1', result["answer"])
            result["answer"] = re.sub(r' +\n', '\n', result["answer"])
        
        return result

        
        
