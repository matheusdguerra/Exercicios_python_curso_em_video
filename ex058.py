# ex058

# gere um numero aleatório de 0 a 10.
# Tente adivinhar até acertar e mostre a quantidade de tentaivas.

from random import randint

numero_aleatorio = randint(0, 10)

tentativas = 0
flag = False

while not flag:
    numero = int(input('Digite um numero entre 0 e 10: '))
    tentativas += 1
    if numero == numero_aleatorio:
        print('Você acertou após {} tentativas!'.format(tentativas))
        flag = True
    else:
        if numero_aleatorio > numero:
            print('Mais...')
        else:
            print('Menos...')

print('Numero do computador: {}\nNumero do usuário: {}'.format(numero_aleatorio, numero))
