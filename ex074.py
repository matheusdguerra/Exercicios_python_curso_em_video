# ex074
# moste um tupla com cinco números aleatórios
# Mostre a listagem da tupla
# mostre o menor e o maior

from random import randint
from random import sample

cont = 0
tupla = sample(range(0, 100), 5)

for c in tupla:
    if cont == 0:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    cont += 1

print(f'Maior: {maior}')
print(f'Menor: {menor}')

for c in tupla:
    print(c, end=' ')


# -----------------------------------


tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

for c in tupla:
    print(c, end=' ')

print(f'\nMaior: {max(tupla)}')
print(f'Menor: {min(tupla)}')
