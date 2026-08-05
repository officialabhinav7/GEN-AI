from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
import os
from langchain_core.runnables import RunnableSequence
load_dotenv()

from langchain_core.output_parsers import StrOutputParser

llm=ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
prompt1=PromptTemplate(
    template="Write a research report about {iit} in 100 words.",
    input_variables=["iit"]
)
parser=StrOutputParser()
sequence=RunnableSequence(prompt1,llm,parser)
output=sequence.invoke({"iit":"IIT Bombay"})
print(output)