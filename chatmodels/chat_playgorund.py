from dotenv import load_dotenv
load_dotenv()

# USING init_chat_model -> this is not availaible in the langChain documentation

# from langchain.chat_models import init_chat_model
# model = init_chat_model(
#     "groq:llama-3.1-8b-instant"
# )

# response = model.invoke("What is cricket?")
# print(response.content)


# USING Model Class

from langchain_groq import ChatGroq
model = ChatGroq(
    model="llama-3.1-8b-instant",   # fast + free tier friendly
    temperature=0,                  # temperature -> more - creative, less - logical
    # max_tokens=20                 # max words llm will generate
)

response = model.invoke("What is cricket?")
print(response.content)
