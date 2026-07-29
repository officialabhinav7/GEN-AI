from langchain.embeddings import GenerativeAIEmbeddings
import numpy as np
import sklearn
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv
load_dotenv()
embeddings = GenerativeAIEmbeddings( model="gemini-3.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
docunments=



