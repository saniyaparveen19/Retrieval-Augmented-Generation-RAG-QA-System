import chromadb
import json
def get_relevant_contexts(question):
  
    client = chromadb.PersistentClient()
    collection = client.get_or_create_collection(name="contexts")


 # finding 3 relevent contexts for each question   
    results = collection.query(
         query_texts=[question],
         n_results=3)
    return results['documents'][0]


    