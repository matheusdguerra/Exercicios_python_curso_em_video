for c in range(0, 6):
    print('Oi')


for c in range(0, 6):
    print(c)
for c in range(1, 7):
    print(c)
for c in range(6, 0, -1):
    print(c)
for c in range(0, 7, 2):
    print(c)

i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
for c in range(i, f+1, p):
    print(c)


for c in range(0, 3):
    n = int(input('Digite um numero: '))
    n += n
print(n)


lista = []
for c in range(0, 3):
    n = input('Digite um numero: ')
    lista.append(n)
print(lista)
