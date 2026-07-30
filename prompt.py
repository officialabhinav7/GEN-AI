import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

st.header("Doing Research About IITs")

choose_iit = st.selectbox(
    "Choose IIT",
    ["IIT Bombay", "IIT Delhi", "IIT Madras", "IIT Kanpur", "IIT Kharagpur"]
)

template = PromptTemplate(
    template="Write a research report about {iit} in 100 words.",
    input_variables=["iit"]
)

prompt = template.invoke({"iit": choose_iit})

if st.button("Generate Research"):
    with st.spinner("Generating report..."):
        result = model.invoke(prompt)
        st.write(st.write(result.content[0]["text"]))