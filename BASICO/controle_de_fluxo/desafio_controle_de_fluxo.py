# Desafio de controle de fluxo
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quanto  senha está incorreta
# - O usuário/senha "corretos" podem ser definidis como
# variáveis dentro do próprio código.

usuario_correto = 'Jobson'
senha_correta = '1234'

usuario = input('Digite o seu usuário: ')
senha = input('Digite sua senha: ')

if usuario == usuario_correto:
    if senha == senha_correta:
        print(f'Acesso liberado, senha bem vindo {usuario}!')
    else:
        print(f'Senha incorreta para o usuário {usuario}')
else:
    print(f'Usuário {usuario} não cadatrado no sistema')

#if usuario == usuario_correto and senha == senha_correta:
#    print('Login concluído com sucesso!')
#elif usuario != usuario_correto and senha != senha_correta:
#    print('usuário e senha incorretos')
#elif usuario != usuario_correto:
#    print('Usuário incorreto')
#elif senha != senha_correta:
#    print('Senha incorreta')



