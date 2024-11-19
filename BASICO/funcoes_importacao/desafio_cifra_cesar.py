def cifrar_caractere(caractere, seq, chave):
    indice_atual = seq.index((caractere))
    novo_indice = indice_atual + chave
    
    # Lidar com indice a direita da sequencia
    while novo_indice >= len(seq):
        novo_indice -= len(seq)
    # Lidar com indice a esquerda da sequencia
    while novo_indice < 0:
        novo_indice += len(seq)
    
    return seq[novo_indice]

texto = 'Não Estou aprendendo Pyhton!'
chave = 26

minus = 'abcdefghijklmnopqrstuvwxyz'
maius = 'ABCEDFGHIJKLMNOPQRSTUVWXYZ'

cifra = ''

for caractere in texto:
    if caractere in minus:
        caractere_cifra = cifrar_caractere(caractere, minus, chave)
    elif caractere in maius:
        caractere_cifra = cifrar_caractere(caractere, maius, chave)
    else:
        caractere_cifra = caractere
    cifra += caractere_cifra

print(cifra)
