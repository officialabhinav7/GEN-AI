from langchain_google_genai import ChatGoogleGenerativeAI
from google.genai.errors import ServerError
import os
from dotenv import load_dotenv

load_dotenv()

models_to_try = [
    "gemini-3.5-flash",       # newest, GA since May 2026
    "gemini-3.1-flash",       # stable fallback
    "gemini-3.1-flash-lite",  # lighter/cheaper fallback
]
result = None
for model_name in models_to_try:
    try:
        llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0.2,
            max_output_tokens=1024,
            top_p=0.8,
            top_k=40,
            max_retries=3,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        result = llm.invoke("Write a short story about a robot learning to love.")
        print(f"✅ Success with {model_name}")
        break
    except ServerError as e:
        print(f"❌ {model_name} unavailable, trying next model...")

if result:
    print(result.content)
else:
    print("All models are currently unavailable. Try again later.")