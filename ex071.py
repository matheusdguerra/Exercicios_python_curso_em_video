# ex071
# Criar um programa que simule um caixa eletrônico
# receba um valor inteiro a ser sacado
# mostre quantas cedulas serão entregues
# Notas -> 50R$, 20R$, 10R$ e 1R$

print('=' * 35)
print('{:^35}'.format('BANCO MATHEUS'))
print('=' * 35)

valor = int(input('Digite o valor a ser sacado: '))

notas_disponiveis = [200, 100, 50, 20, 10, 5, 1]
cursor_notas_disponiveis = 0

while cursor_notas_disponiveis < len(notas_disponiveis):

    notas_entregues = valor // notas_disponiveis[cursor_notas_disponiveis]
    valor = valor - (notas_entregues * notas_disponiveis[cursor_notas_disponiveis])

    if notas_entregues > 0:
        print(f'Notas de R${notas_disponiveis[cursor_notas_disponiveis]} -> {notas_entregues}')

    cursor_notas_disponiveis += 1

print('=' * 35)
print('{:^35}'.format('VOLTE SEMPRE'))
print('=' * 35)
