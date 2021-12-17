# ex023
# receba um numero de 4 caracteres (0 a 9999) e mostra os difgitos separados
# 8768
# unidade: 8
# dezena: 6
# centena: 7
# milhar: 8

numero = int(input('Digite um numero: '))

print('Unidade {}'.format(numero // 1 % 10))
print('Dezena {}'.format(numero // 10 % 10))
print('Centena {}'.format(numero // 100 % 10))
print('Milhar {}'.format(numero // 1000 % 10))
