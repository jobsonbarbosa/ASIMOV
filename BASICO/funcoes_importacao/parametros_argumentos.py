def somar_dois(n): # paramentro
    return n + 2

x = 10 # argumento

resultado = somar_dois(x)

print(resultado)


def adicionar_final(texto, final = ' Barbosa'):# valor padrão pode ser incluido no paramentro
    return texto + final

print(adicionar_final('Jobson')) # para usar o parametro padrão, pode omitir o arquimento da função e o paramentro é passado automaticamente

def dividir(a, b):
    if b == 0:
        return 'Impossível dividir!'
    return a / b 

print(dividir(a=10, b=0))