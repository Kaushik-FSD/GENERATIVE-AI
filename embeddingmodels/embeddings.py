from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=64
)

vector = embeddings.embed_query("This is gen AI course")

# Paid model, needs quota plan
print(f"VECTOR EMBEDDING :: {vector}")