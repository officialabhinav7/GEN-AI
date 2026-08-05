from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplete
from dotenv import load_dotenv
import os
from langchain_core.runnables import RunnableSequence
load_dotenv()

llm=ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
prompt1=PromptTemplete(
    template="Write a research report about {iit} in 100 words.",
    input_variables=["iit"]
)
