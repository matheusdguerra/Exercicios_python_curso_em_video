# ex050
# receba 6 numero e some apenas os pares, se o numero for impar desconsidere-o

soma = 0

for c in range(0, 5):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
    else:
        print('numero desconsiderado')

print(soma)
