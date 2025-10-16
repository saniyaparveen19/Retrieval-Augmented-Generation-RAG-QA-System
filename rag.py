import json
import chromadb
from tqdm import tqdm
# --- 1. Load your JSON data ---
# For this example, the JSON data is stored in a multiline string.
# In a real scenario, you would load it from a file like this:
with open('squad.json', 'r') as f:
    data = json.load(f)

all_qas = []
contexts = []
metadatas = []
document_ids = []
doc_counter = 1

# --- 3. Iterate through the JSON structure ---
# The main content is in the "data" key
for article in tqdm(data['data'][0:10]):
    # Each article has a list of "paragraphs"
    for paragraph in article['paragraphs']:
        # This is the context we want to store as a document
        context_text = paragraph['context']
        contexts.append(context_text)
        
        # This is the list of question-answer objects
        qas = paragraph['qas']
        
        # Objective 1: Add all qa objects to a single list
        all_qas.extend(qas)
        
        # Objective 2: Extract qa ids for the metadata
        qa_ids = [qa['id'] for qa in qas]
        qa_str = ', '.join(qa_ids)
        metadatas.append({'qa_ids': qa_str})
        
        # Create a unique ID for this document (context)
        document_ids.append(f"context_{doc_counter}")
        doc_counter += 1

# --- 4. Setup ChromaDB and create a collection ---
# Using an in-memory ephemeral client. For persistence, use chromadb.PersistentClient(path="/your/db/path")
client = chromadb.PersistentClient() 
collection = client.get_or_create_collection(name="contexts")

# --- 5. Add the processed data to the ChromaDB collection ---
collection.add(
    documents=contexts,
    metadatas=metadatas,
    ids=document_ids
)

# --- 6. Verification ---
print("✅ ChromaDB collection populated successfully!")
print(f"Total number of documents in collection: {collection.count()}")
print("\n")
print("First document added to ChromaDB:")
print(collection.get(ids=['context_1']))
print("\n" + "="*50 + "\n")

print(f"Total number of QA objects collected: {len(all_qas)}")
print("\nFirst 3 QA objects in the consolidated list:")
# Using json.dumps for pretty printing
print(json.dumps(all_qas[:3], indent=4))

# --- 7. Save the consolidated QA list to a JSON file ---
with open('all_qas.json', 'w') as f:
    json.dump(all_qas, f, indent=4)