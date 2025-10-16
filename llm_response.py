import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
def get_llm_response(prompt):

    gemini_api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=gemini_api_key)

    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt)
    return getattr(response, "text", None) or getattr(response, "output_text", "")