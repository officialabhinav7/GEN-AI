from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Prompt 1: Generate report
prompt1 = PromptTemplate(
    template="Write a research report about {iit} in 100 words.",
    input_variables=["iit"]
)

# Prompt 2: Summarize report
prompt2 = PromptTemplate(
    template="Summarize the following research report in 50 words:\n\n{report}",
    input_variables=["report"]
)

parser = StrOutputParser()

# First chain
report_sequence = prompt1 | llm | parser

# Second chain
summary_sequence = prompt2 | llm | parser

# Connect both chains
chain = (
    report_sequence
    | RunnableLambda(lambda report: {"report": report})
    | summary_sequence
)

result = chain.invoke({"iit": "IIT Bombay"})
print(result)