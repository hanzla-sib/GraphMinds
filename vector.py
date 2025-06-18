from langchain_ollama import OllamaEmbeddings

from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "restaurant_reviews.csv")
df = pd.read_csv(csv_path)

embeddings = OllamaEmbeddings(model="llama3.1")
db_location='./chroma_db'
add_documents = not os.path.exists(db_location)
print(f"Adding documents to ChromaDB: {add_documents}")
if add_documents:
    print("Creating new ChromaDB database...")
if add_documents:
    documents = []
    ids = []
    for i, row in df.iterrows():
        doc = Document(page_content=row['Title'] + " " + row['Review'], metadata={"rating": row['Rating'],"date": row['Date']})
        documents.append(doc)
        ids.append(str(i))
        
vector_store = Chroma(collection_name="restaurant_reviews",persist_directory=db_location,
                      embedding_function=embeddings)
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)