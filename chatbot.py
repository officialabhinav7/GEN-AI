from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
load_dotenv()
model=ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]
while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content[0]["text"]))
    print("AI: ",result.content[0]["text"])

print(chat_history)