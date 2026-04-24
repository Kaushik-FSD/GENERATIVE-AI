from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

print("press 1 for happy mode, 2 for sad mode, 3 for angry mode")
mode = int(input("Enter the mode: "))

print("---------- Chat Bot ----------")
print("Type 'quit' to end the conversation")
print("------------------------------")

if mode == 1:
    system_message = "you are a funny AI assistant, you respond with a lot of emojis and funny words"
elif mode == 2:
    system_message = "you are a sad AI assistant, you respond with a lot of emojis and sad words"
elif mode == 3:
    system_message = "you are an angry AI assistant, you respond agressively and impatiently"

# to store chat convo we can add a list for now:
messages = [
    SystemMessage(content=system_message)  #This is the system message that will be used to guide the AI's behavior
]

while True:
    user_input = input("You: ")
    # append the user input to the messages list
    messages.append(HumanMessage(content=user_input))  #adding the HumanMessage to the messages list
    print("\n")

    if user_input.lower() == "quit":
        break

    # response = model.invoke(user_input)

    # this will use the chat history to generate the response
    response = model.invoke(messages)  
    messages.append(AIMessage(content=response.content))  #adding the AIMessage to the messages list

    print(f"ChatBot: {response.content} \n")