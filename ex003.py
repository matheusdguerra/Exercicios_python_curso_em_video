
# Tipos primitivos

from typing import no_type_check

valorA = input('Digite valor A: ')
valorB = int(input('Digite valor B: '))

soma = int(valorA) + valorB
print('A soma de {} com {} é {}'.format(valorA, valorB, soma))
print(f'A soma entre {valorA} e {valorB} é igual a: {soma}')

algo = input('digite algo: ')
print(type(algo))
print(algo.isnumeric())

algo = input('digite algo: ')
print(type(algo))
print(algo.isalpha())

algo = input('digite algo: ')
print(type(algo))
print(algo.isalnum())
