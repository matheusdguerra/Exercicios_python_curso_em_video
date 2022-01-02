# ex078
# leia 5 valores e guareos em uma lista
# mostre o maior e o menor e as suas posições.

lista = []

for cont in range(0, 5):
    lista.append(int(input(f'Digite o {cont + 1}º valor: ')))
'''
max_value = max(lista)
min_value = min(lista)

print(f'O maior numero é: {max_value} na posição: {lista.index(max_value) + 1}')
print(f'O menor numero é: {min_value} na posição: {lista.index(min_value) + 1}')

# ---------------------------------------------------------------------------------
max_value = 0
min_value = 0
indices_maiores = []
indices_menores = []

for idx, cont_maior in enumerate(lista):
    if cont_maior >= max_value:
        max_value = cont_maior
        indices_maiores.append(idx)

for idx, cont_menor in enumerate(lista):
    if cont_menor <= min_value:
        min_value = cont_menor
        indices_menores.append(idx)

print(f'O maior valor digita foi {max_value} nas posições', end=' ')
for c in indices_maiores:
    print(f'{c}...', end=' ')

print(f'\nO menor valor digita foi {min_value} nas posições', end=' ')
for c in indices_menores:
    print(f'{c}...', end=' ')
'''

max_value = max(lista)
min_value = min(lista)

print(f'O maior numero digitado é {max_value} nas posições ', end='')
for idx, c in enumerate(lista):
    if c == max_value:
        print(idx, end='... ')

print(f'\nO menor numero digitado é {min_value} nas posições ', end='')
for idx, c in enumerate(lista):
    if c == min_value:
        print(idx, end='... ')
