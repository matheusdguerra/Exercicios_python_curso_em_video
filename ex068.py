# ex068
# jogue par ou impar com o computador
# O jogo só termina quando o jogador perder

from random import randint, choice

vitorias = 0

while True:
    numero_jogador = int(input('Digite um numero: '))
    escolha_jogador = str(input('Par ou Impar [P/I]: '))

    numero_computador = randint(0, 9)
    soma = numero_computador + numero_jogador

    if escolha_jogador in 'Pp' and ((numero_computador + numero_jogador) % 2) == 0:
        print('Jogador venceu!')
        vitorias += 1
    elif escolha_jogador in 'Ii' and ((numero_computador + numero_jogador) % 2) == 1:
        print('Jogador Venceu!')
        vitorias += 1
    else:
        print('Computador venceu!')
        break

print(f'Você ganhou {vitorias}')
