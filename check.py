from llm_response import get_llm_response

def validate_answer(question, ai_answer, correct_answer):
    prompt = f"""You are a validation AI. Your task is to determine if the AI-generated answer 
    to a question is correct based on the provided correct answer.
    """
    prompt += f"""Question: {question}
    AI-generated Answer: {ai_answer}
    Correct Answer: {correct_answer}

    if the answer is correct, respond with "Correct". If the answer is incorrect, 
    respond with "Incorrect".
"""
    validation_response = get_llm_response(prompt)
    if "correct" in validation_response.lower():
        return True
    else:
        return False
    