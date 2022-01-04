# ex087
# crie uma matriz de 3 por 3 preenchendo os valores pelo teclado
# no final mostre:
# -> a soma dos valores pares
# -> a soma dos valores da terceira coluna
# o maior valor da segunda linha

lista = []
lista_0 = []
lista_1 = []
lista_2 = []
lista.append(lista_0)
lista.append(lista_1)
lista.append(lista_2)
soma_terceira_coluna = soma_pares = maior_segunda_linha = 0

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

for l in lista:
    for c in l:
        if c % 2 == 0:
            soma_pares += c

for c in lista:
    soma_terceira_coluna += c[2]

for c in lista[1]:
    if c == 0:
        maior_segunda_linha = c
    else:
        if maior_segunda_linha < c:
            maior_segunda_linha = c


print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')

l = 0
for c in range(0, 3):
    print(lista[c][l], lista[c][l+1], lista[c][l+2], end='\n')
