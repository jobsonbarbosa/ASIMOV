import requests

print("ativando assistente")

def perguntar(questao):
    url = "http://localhost:11434/api/chat"
    data = {
        "model": "llama3.2",
        "messages": [
            {"role": "user", "content": questao}
        ],
        "stream":False
    }

    return requests.post(url, json=data)

while True:
    pergunta = input ("Voce: ")
    if pergunta.lower() == "sair":
        break
    
    resposta = perguntar(pergunta)
    print(resposta)
    # print("Se der 200 a resposta deu boa:", resposta.status_code)
    print(resposta.json()['model'] + ":", resposta.json()['message']['content'])

print('desligando')