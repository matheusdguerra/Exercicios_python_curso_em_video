# ex091
# Monte um programa onde 4 jogadores jogem um dado e tenham resultados [1~6] aleatório
# Guarde o resultado em um dicionário
# no final coloque o dicionario em ordem sabendo que o vencedor tirou o número maior

from time import sleep
from random import randint
from operator import itemgetter

jogadas = []
jogadas_temp = {}

for c in range(0, 4):
    jogadas_temp['nome'] = f'jogador{c+1}'
    jogadas_temp['valor'] = randint(1, 6)
    jogadas.append(jogadas_temp.copy())

print('\nValores sorteados')
for v in range(0, 4):
    print(f'O {jogadas[v]["nome"]} tirou {jogadas[v]["valor"]}')
    sleep(1)


# Faz o sort
jogadas_ordenadas = sorted(jogadas, key=lambda row: (row['valor'], row['nome']), reverse=1)

print('\nRanking dos jogadores')
for v in range(0, 4):
    print(f'{v+1}º Lugar -> {jogadas_ordenadas[v]["nome"]} tirou {jogadas_ordenadas[v]["valor"]}')
    sleep(1)
