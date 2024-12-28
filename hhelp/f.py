# hhelp/f.py
import os
from .config import genai
from .utils import convert_file

def f(file_path):
    converted_path, mime_type = convert_file(file_path)
    uploaded = genai.upload_file(
        path=converted_path,
        display_name=os.path.basename(converted_path),
        mime_type=mime_type
    )
    model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp")
    prompt = "Please give clearly separate, running code for all the questions in this. Just give the code, with question at the top in the comment, nothing else"
    response = model.generate_content([prompt, uploaded])
    return response.text
