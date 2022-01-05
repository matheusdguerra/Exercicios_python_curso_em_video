# ex085
# Leia sete valores numéricos e cadastre os em uma lista única separdado por uma lista de pares e uma lista de impares
# no final mostre os valores pares e impares em ordem crescente
'''
lista = []
lista_pares = []
lista_impares = []
lista.append(lista_pares)
lista.append(lista_impares)

print(lista)

for c in range(0, 7):
    numero = int(input(f'Digite o {c+1}º número: '))
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

lista_impares.sort()
lista_pares.sort()

print(lista)

'''

lista = [[], []]

for c in range(0, 7):
    numero = int(input(f'Digite o {c+1}º número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

lista[0].sort()
lista[1].sort()

print(lista[0])
print(lista[1])
