from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')

#configurando o modelo de chat

chat = ChatGroq(temperature=0, model="llama3-70b-8192")

prompt = ChatPromptTemplate.from_messages([
    ("system", "Voce é uma assintente amigavél"),
    ("human", "{input}"),
])

chain = prompt | chat

# invocando o modelo
response = chain.invoke({"input": "Explique a importancia das IA para a humanindade"})

# print(response.content)

for trecho in chain.stream(response):
    print(trecho.content, end='')