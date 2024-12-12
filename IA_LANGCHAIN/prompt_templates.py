from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')

prompt_template = PromptTemplate.from_template('''
Responda a seguinte pergunta do usuário: {pergunta}
                                               ''')

print(prompt_template.format(pergunta = 'O que é materia escuro?'))
