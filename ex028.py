# ex028
# gere um numero aleatório de 0 a 5.
# Receba um numero de 0 a 5 e teste se é o mesmo numero gerado aleatóriamente

from random import choices

numero_aleatorio = str(choices([0, 1, 2, 3, 4, 5]))

numero = input('Digite um numero entre 0 e 5: ')
numero = '[' + numero + ']'

print(numero, numero_aleatorio)

if numero == numero_aleatorio:
    print('Você acertou!')
else:
    print('Você errou!')
