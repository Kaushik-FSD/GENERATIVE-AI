from dotenv import load_dotenv

load_dotenv()

import os
from langchain_groq import ChatGroq

model = ChatGroq(
    model="llama-3.1-8b-instant",   # fast + free tier friendly
    temperature=0
)

# print(f"LLM :: {llm}")

response = model.invoke("What is cricket?")
print(response.content)

