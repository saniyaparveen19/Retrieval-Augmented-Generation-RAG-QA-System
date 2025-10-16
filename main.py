import json
from llm_response import get_llm_response
from dotenv import load_dotenv
import os
from get_contexts import get_relevant_contexts
from llm_answers import generate_answer
from check import validate_answer


# Loading the quesions
with open('all_qas.json', 'r') as f:
    all_qas = json.load(f)


#loop through each question and get answer
answers = []
validation_results = []
for i, qa in enumerate(all_qas[0:20]):  
    question = qa["question"]
   # contexts= "\n\n".join (qa['contexts'])
    contexts = get_relevant_contexts(question)
   
    answer = generate_answer(question, contexts)
    validation_result = validate_answer(question, answer, qa["answers"][0]["text"])
    validation_results.append({
        "question": question,
        "ai_answer": answer,
        "correct_answer": qa["answers"][0]["text"],
        "is_correct": validation_result
    })
    print(f"\n🔹 Question {i+1}: {question}")
    print(f"Answer: {answer}")
    print("\n" + "="*80 )

# Save the answers to a new json file
with open('llm_validation_results.json', 'w') as f:
    json.dump(validation_results, f, indent=4)