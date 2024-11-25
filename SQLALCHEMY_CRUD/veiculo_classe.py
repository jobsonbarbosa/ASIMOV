

class Veiculo:
    
    rodas = None
    
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.ligado = False

    def descricao(self):
        print(f'Meu modelo é {self.modelo} e minha cor é {self.cor}')
        
    def ligar(self):
        self.ligado= True
        print(f'O veiculo foi ligado')
        
    def desligar(self):
        self.ligado = False
        print(f'O veliculo foi desligado')
    
    def pintar(self, nova_cor):
        self.cor = nova_cor
        print(f'O veiculo foi pintado. Nova cor {self.cor}')

# Herança
class Carro(Veiculo):
    rodas = 4
    def descricao(self):
        print(f'Eu sou um carro, meu modelo é {self.modelo} e minha cor: {self.cor} e possui {self.rodas} rodas')
        
meu_carro = Carro(cor='Azul', modelo='Onix Plus')
meu_carro.descricao()
meu_carro.pintar('Vermelho')
res = input('L para ligar | D para desligar\n')
if res == 'd':
    meu_carro.desligar()
else:
    meu_carro.ligar()
