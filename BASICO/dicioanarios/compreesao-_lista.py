valores = list(range(15))

maiores_que_cinco = []

# for valor in valores:
#     if valor > 5:
#         maiores_que_cinco.append(valor)

maiores_que_cinco = [
    valor # resultado
    for valor in valores # para cada elemento in sequencia
    if valor > 5 # se condição
]
        
print(valores)
print(maiores_que_cinco)