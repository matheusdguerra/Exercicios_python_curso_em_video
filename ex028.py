# ex028
# gere um numero aleatório de 0 a 5.
# Receba um numero de 0 a 5 e teste se é o mesmo numero gerado aleatóriamente

from random import choices, randint
from time import sleep

numero_aleatorio = randint(0, 5)

numero = int(input('Digite um numero entre 0 e 5: '))


print('Processando...')
sleep(3)

if numero == numero_aleatorio:
    print('Você acertou!')
else:
    print('Você errou!')

print('Numero do computador: {}\nNumero do usuário: {}'.format(numero_aleatorio, numero))
