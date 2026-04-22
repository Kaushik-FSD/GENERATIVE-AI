from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    # repo_id="meta-llama/Meta-Llama-3-8B-Instruct"
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Explain recursion with a real-life analogy")
print(response.content)