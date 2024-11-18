palavra = 'Olá MunDo!'

print(palavra.lower())
print(palavra.upper())

arquivo = '2024_11_10_Nota_Fical.pdf'
print(arquivo.endswith('.pdf'))

print(arquivo.startswith('2024'))

texto = 'O que sabemos é uma gota, o que ignoramos um oceano'

print(texto.count('a'))

print(texto.count('que'))

seq = 'aaaaaaabbbbbabababaab'

print(seq.find('b'))

s1 = '12987318273918'
print(s1.isdigit()) # verificar se contém apenas numeros

s2 = 'sdfaskjhdfaksjh'
print(s2.isalpha()) # verifica se contém apenas string


frase = 'Estou estudando Python!'
print(frase.replace('!', '?'))

print(frase.replace('Python', 'Jaascript'))