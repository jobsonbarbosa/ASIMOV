# Escreva o seu código aqui :-)
# combinas diverentes valores de true or false

print('------ INÍCIO ------\n')

estou_com_fome = input('Estou com fome? (Digite s para sim)\n') == 's'
tenho_comida = input('Tenho comida? (Digite s para sim)\n') == 's'

if estou_com_fome and not tenho_comida:
    print('Ir ao mercado')
    print('Voltar para casa')
    print('Preparar uma refeição')
    print('Comer a comida')

if estou_com_fome and tenho_comida:
    print('Preparar uma refeição')
    print('Comer a comida')

prin('\n------ FIM ------')
