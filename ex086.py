# ex086
# crie uma matriz de 3 por 3 preenchendo os valores pelo teclado
# no final mostre os valores no fromato matriz 3 por 3
'''
lista = []
lista_0 = []
lista_1 = []
lista_2 = []
lista.append(lista_0)
lista.append(lista_1)
lista.append(lista_2)

print(lista)

for c in range(0, 3):
    for l in range(0, 3):
        numero = int(input(f'Digite o valor para [{c}, {l}]º número: '))
        if c == 0:
            lista_0.append(numero)
        if c == 1:
            lista_1.append(numero)
        if c == 2:
            lista_2.append(numero)

l = 0
for c in range(0, 3):
    print(lista[c][l], lista[c][l+1], lista[c][l+2], end='\n')

print(lista[0][0], lista[0][1], lista[0][2])
print(lista[1][0], lista[1][1], lista[1][2])
print(lista[2][0], lista[2][1], lista[2][2])


for l in lista:
    for c in l:
        print(f' {c} ', end='')
    print('\n')
'''

'''
lista = [[], [], []]

for c in range(0, 3):
    for l in range(0, 3):
        numero = int(input(f'Digite o valor para [{c}, {l}]º número: '))
        lista[l].append(numero)

print(lista)
l = 0
for c in range(0, 3):
    print(lista[l][c], lista[l+1][c], lista[l+2][c], end='\n')
'''

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0, ]]

for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite o valor para [{l}, {c}]º número: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^6}]', end='')
    print()
