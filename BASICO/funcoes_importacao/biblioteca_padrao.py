import math
import datetime
import random
import os
import time

print(math.pi)
print(math.log(16,2))

print(datetime.datetime.now())
agora = datetime.datetime.now()
ano_2000 = datetime.datetime(2000,1,1)
print(agora - ano_2000)

for _ in range(5):
    n = random.randint(1, 20)
    print(f'Número escolhifo: {n}')
    
nomes = ['Jobson', 'Joelma', 'Carolina']
for _ in range(5):
    nome = random.choice(nomes)
print(f'Nome escolhido: {nome}')


print(os.getcwd())
print(os.listdir())

inicio = time.time()
print('Primeira linha')
time.sleep(3)
print('Segunda linha')

final = time.time()
tempo_execucao = final - inicio
print(f'Demorou {tempo_execucao:.3f} segundo para executar')