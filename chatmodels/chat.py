from dotenv import load_dotenv

load_dotenv()

import os

# USING Model Class

# from langchain_groq import ChatGroq
# model = ChatGroq(
#     model="llama-3.1-8b-instant",   # fast + free tier friendly
#     temperature=0
# )

# response = model.invoke("What is cricket?")
# print(response.content)

# USING init_chat_model -> this is not availaible in the langChain documentation

from langchain.chat_models import init_chat_model
model = init_chat_model(
    "groq:llama-3.1-8b-instant"
)

response = model.invoke("What is cricket?")
print(response.content)

