# hhelp/a.py
from .config import genai

def a(question):
    model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp")
    response = model.generate_content([question])
    return response.text
