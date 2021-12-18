# ex033
# leia três números. Mosre o menor e o maior número

from random import sample

lista_numeros = sample(range(0, 100), 3)
print(lista_numeros)

# testa maior número
if lista_numeros[0] > lista_numeros[1] and lista_numeros[0] > lista_numeros[2]:
    maior_numero = lista_numeros[0]
elif lista_numeros[1] > lista_numeros[2]:
    maior_numero = lista_numeros[1]
else:
    maior_numero = lista_numeros[2]

# testa menor número
if lista_numeros[0] < lista_numeros[1] and lista_numeros[0] < lista_numeros[2]:
    menor_numero = lista_numeros[0]
elif lista_numeros[1] < lista_numeros[2]:
    menor_numero = lista_numeros[1]
else:
    menor_numero = lista_numeros[2]

print('O maior número é {}'.format(maior_numero))
print('O menor número é {}'.format(menor_numero))
