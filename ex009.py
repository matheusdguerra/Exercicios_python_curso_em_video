# ex009
# Receba um numero inteiro e mostre a sua tabuada

numero = int(input('Digite um número: '))

n = 0

while (n <= 10):
    print('{} x {} = {}'.format(n, numero, n * numero))
    n += 1
