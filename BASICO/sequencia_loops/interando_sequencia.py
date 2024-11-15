clientes = [
    ('Jobson', 'xxx', 'xxx@email.com'), 
    ('Jomesson', 'xxx', 'xxx@email.com')
]
# for cliente in clientes:
#     nome = cliente[0]
#     cpf = cliente[1]
#     email = cliente[2]
#     print(f'Cliente: {nome}\nCPF: {cpf}\nEmail: {email}\n\n')

#-------- Ou forma de exibir o FOR

for cliente in clientes:
    nome, cpf, email = cliente
    print(f'Cliente: {nome}\nCPF: {cpf}\nEmail: {email}\n\n')
    
print('Acabou!')