# ex047
# mostre a lista de numeros pares de 1 até 50

for c in range(1, 51):
    if c % 2 == 0:
        print(c)


lista = []
for c in range(1, 51):
    if c % 2 == 0:
        lista.append(c)
print(lista)
