# ex068
# jogue par ou impar com o computador
# O jogo só termina quando o jogador perder

from random import randint, choice

vitorias = 0
escolha_jogador = ' '

while True:
    numero_jogador = int(input('Digite um numero: '))

    escolha_jogador = ' '
    while escolha_jogador not in 'PI':
        escolha_jogador = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]

    numero_computador = randint(0, 9)
    soma = numero_computador + numero_jogador

    print(f'Deu PAR!' if soma % 2 == 0 else 'Deu IMPAR!')

    if escolha_jogador in 'P' and soma % 2 == 0:
        print('Jogador venceu!')
        print('+-' * 20)
        vitorias += 1
    elif escolha_jogador in 'I' and soma % 2 == 1:
        print('Jogador Venceu!')
        print('+-' * 20)
        vitorias += 1
    else:
        print('Computador venceu!')
        break

print(f'Você ganhou {vitorias}')
