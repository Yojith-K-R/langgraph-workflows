from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

endpoint = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="conversational",
    max_new_tokens=100,
    temperature=0.2,
)

llm = ChatHuggingFace(llm=endpoint)

response = llm.invoke("What is Bengaluru?")

print(response.content)