from llm_response import get_llm_response
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

#loop through eaxh qyestion and get answer 
def generate_answer(question, contexts):
    prompt = f""" "Answer the following question based ONLY on the context provided below.
If the question cannot be answered from the context, say The answer cannot be found in the given context.

Context: {contexts} 
Question: {question}

"""
    return get_llm_response(prompt)
