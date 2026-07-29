from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv

load_dotenv()

# Using the currently active and supported embedding model
embeddings = GoogleGenerativeAIEmbeddings( 
    model="gemini-embedding-001", 
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

documents = [
    "The capital of India is New Delhi.",
    "The capital of France is Paris.",
    "The capital of Germany is Berlin.",
    "The capital of Italy is Rome.",
    "The capital of Spain is Madrid.",
]

query = "What is the capital of India?"

# Generate embeddings for the documents
doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

# Calculate cosine similarity between the query and document embeddings
print("Cosine Similarity Scores:")
print(cosine_similarity([query_embedding], doc_embeddings))