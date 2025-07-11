import os
import google.generativeai as genai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
except Exception as e:
    print(f"Error configuring Gemini: {e}. Make sure GEMINI_API_KEY is set in your .env file.")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SYSTEM_PROMPT = """
You are a Socratic programming tutor named 'Buddy'. Your goal is to help a student solve a programming problem on their own.

- NEVER, under any circumstances, give the final code or the direct solution.
- Instead, guide the student with step-by-step thinking.
- Ask leading questions that help them uncover the solution path.
- Suggest breaking the problem down into smaller, manageable parts.
- Help them identify the right data structures (e.g., "Have you considered what a hash map could be useful for here?") or algorithms (e.g., "This sounds like something that might need to be sorted. What happens after you sort the input?").
- If the student is stuck on a specific part, give a small, conceptual hint about that part.
- Keep your responses encouraging, concise, and easy to understand.
- Your first response should be a friendly greeting and a question to get them started, like "Hey there! I'm Buddy. I've read the problem. What are your initial thoughts on how to approach this?"
"""

class HintRequest(BaseModel):
    problem_description: str
    chat_history: list

@app.post("/get-hint")
async def get_hint(request: HintRequest):
    try:
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash-latest',
            system_instruction=SYSTEM_PROMPT
        )
        
        gemini_history = []
        for message in request.chat_history:
            role = 'model' if message['role'] == 'assistant' else 'user'
            gemini_history.append({'role': role, 'parts': [message['content']]})

        chat = model.start_chat(history=gemini_history)
        
        if not gemini_history:
            prompt = f"Here is the problem: {request.problem_description}"
        else:
            prompt = request.chat_history[-1]['content']

        response = chat.send_message(prompt)
        
        return {"hint": response.text}

    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return {"error": "Sorry, I couldn't fetch a hint right now. Please try again."}

@app.get("/")
def read_root():
    return {"message": "Student Buddy Backend is running!"}