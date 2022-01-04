# ex088
# Simulador de mega-sena
# Receba a quantidade de jogos e sortei 6 numeros (entre 1 e 60 em repetir) para cada jogada
# tudo em uma lista composta

from random import sample
from time import sleep

print_jogo = 1
lista_valores_papite = []

palpites = int(input('Quantas jogadas deseja simular? '))

for c in range(0, palpites):

    valores_palpite = sample(range(0, 60), 6)
    lista_valores_papite.append(valores_palpite)
    # print(lista_valores_papite)
    # lista_valores_papite.clear()
for c in lista_valores_papite:
    c.sort()
    print(f'Jogo {print_jogo}:  {c}')
    sleep(1)
    print_jogo += 1
print(lista_valores_papite)
