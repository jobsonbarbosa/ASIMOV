import langchain_llama
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.environ['GROQ_API_KEY']

llm = Llama(api_key=groq_api_key)

print(llm)
# pergunta = "Escreva um texto sobre IA"

# for trecho in llm.stream(pergunta):
#     print(trecho, end='')