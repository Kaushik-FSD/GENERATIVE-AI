from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

print("---------- Chat Bot ----------")
print("Type 'quit' to end the conversation")
print("------------------------------")

# to store chat convo we can add a list for now:
messages = []

while True:
    user_input = input("You: ")
    # append the user input to the messages list
    messages.append(user_input)
    print("\n")

    if user_input.lower() == "quit":
        break

    # response = model.invoke(user_input)

    # this will use the chat history to generate the response
    response = model.invoke(messages)  
    messages.append(response.content)

    print(f"ChatBot: {response.content} \n")