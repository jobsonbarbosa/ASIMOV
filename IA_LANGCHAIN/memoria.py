# integração de uma Memoria com o chain

from dotenv import load_dotenv
import os

from langchain.memory import ConversationBufferMemory
from llama_cpp import llama

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

# print(api_key)

# #carregando o pacote
# memoria = ConversationBufferMemory()

# #adicionando memorias de forma manual
# memoria.chat_memory.add_user_message('Oi?')
# memoria.chat_memory.add_ai_message('Como vai?')

# #carrega o dicionário em um variavel para ser imprimida
# resp = memoria.load_memory_variables({})

#===============================
# Outra forma 
# memoria = ConversationBufferMemory(return_messages=True)
# memoria.chat_memory.add_user_message('Oi?')
# memoria.chat_memory.add_ai_message('Como vai?')
# resp = memoria.load_memory_variables({})

# print(resp)


# =================
# Conversar em momeria com a Openain

from langchain_openai.chat_models import ChatOpenAI
from langchain.chains.conversation.base import ConversationChain

chat = ChatOpenAI()

memoria = ConversationBufferMemory()

#   usado o verbose = True todas as conversão serão printadas
conversa = ConversationChain(llm=chat, memory=memoria, verbose=True)

# informando no nome, será que manteve na memoria, vamos comentar este codigo
conversa.predict(input='Olá Meu nome é Jobs')

conversa.predict(input='Qual é o meu nome?')

print(conversa)