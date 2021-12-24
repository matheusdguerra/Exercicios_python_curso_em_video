# ex049
# Receba um numero inteiro e mostre a sua tabuada


numero = int(input('Digite um número: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(c, numero, c * numero))


for c in range(0, 11):
    print('+-' * 7)
    print('Tabuada do {}'.format(c))
    for c2 in range(0, 11):
        print('{} x {} = {}'.format(c, c2, c * c2))
