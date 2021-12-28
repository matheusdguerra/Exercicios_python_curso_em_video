# ex058

# gere um numero aleatório de 0 a 10.
# Tente adivinhar até acertar e mostre a quantidade de tentaivas.

from random import choices, randint
from time import sleep

numero_aleatorio = randint(0, 10)

tentativas = 0
flag = True

while flag == True:
    numero = int(input('Digite um numero entre 0 e 10: '))

    print('Processando...')
    sleep(1)

    if numero == numero_aleatorio:
        print('Você acertou após {} tentativas!'.format(tentativas + 1))
        flag = False
    else:
        print('Você errou!\nTente novamente')
        tentativas += 1

print('Numero do computador: {}\nNumero do usuário: {}'.format(numero_aleatorio, numero))
