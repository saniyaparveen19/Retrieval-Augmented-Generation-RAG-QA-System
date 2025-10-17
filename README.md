# 🧠 Retrieval-Augmented Generation (RAG) QA System

A complete Retrieval-Augmented Generation pipeline built with ChromaDB and Google Gemini — designed to retrieve relevant contexts and generate accurate answers validated against the SQuAD dataset.

🔍 Overview

This project implements a RAG-based Question Answering System that integrates:

ChromaDB → for semantic search and context retrieval

Google Gemini API → for generating responses

SQuAD dataset → for validation and evaluation

The system retrieves top relevant contexts, generates answers using Gemini, and validates them against ground truth data from SQuAD to measure accuracy.

⚙️ Workflow

Load & process SQuAD JSON dataset.

Store contexts and metadata in ChromaDB.

Save all Q&A pairs in all_qas.json.

Retrieve top 3 relevant contexts for each question.

Generate answers using Google Gemini LLM.

Validate answers with the original dataset.

Export results to llm_validation_results.json.

🧩 Features

Efficient semantic context retrieval with ChromaDB

Answer generation via Google Gemini LLM

Validation against SQuAD ground-truth answers

Modular design for easy experimentation and scaling

Clear JSON-based storage structure for reproducibility

🗂️ Project Structure
rag_qa_project/
├── squad.json                # Original SQuAD dataset
├── all_qas.json              # Consolidated Q&A pairs
├── qa_with_contexts.json     # Questions + retrieved contexts
├── create_chromadb.py        # Load and populate ChromaDB
├── get_contexts.py           # Retrieve relevant contexts
├── llm_response.py           # Gemini API wrapper
├── llm_answers.py            # Generate answers
├── validate_results.py       # Run answer generation + validation
├── check.py                  # Compare AI vs original answers
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation

🧰 Setup Instructions

1️⃣ Prerequisites

Python 3.10+

Install dependencies:

pip install -r requirements.txt

2️⃣ Environment Setup

Create a .env file in the project root and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

🚀 How to Run
Step 1: Create the ChromaDB Collection
python create_chromadb.py

Extracts and stores dataset contexts and metadata into ChromaDB.

Step 2: Generate and Validate Answers
python validate_results.py

Retrieves top contexts, generates answers with Gemini, and validates them against the original dataset.

📊 Output Example

Results are stored in llm_validation_results.json as:

{
  "question": "When did Beyonce start becoming popular?",
  "ai_answer": "in the late 1990s",
  "correct_answer": "in the late 1990s",
  "is_correct": true
}

You can analyze this file to check model accuracy and consistency.

🧪 Technical Details

ChromaDB  -  Stores dataset contexts and performs semantic retrieval
Google Gemini  -  Generates answers from provided contexts
SQuAD Dataset -   Provides ground-truth for validation
JSON Files  -  Maintain structured QA pairs and validation results

📈 Future Improvements

Add accuracy, precision, recall & F1-score metrics

Batch process large-scale datasets

Add evaluation dashboard

Explore LangChain or LlamaIndex integrations for modular RAG pipelines

📦 Dependencies
chromadb==0.4.14
google-generativeai==0.2.0
tqdm==4.66.1
python-dotenv==1.0.1

Install with:

pip install -r requirements.txt

🧑‍💻 Author

Developed by: [saniya parveen]
Purpose: Educational / Research – Building RAG QA pipeline with open tools.


