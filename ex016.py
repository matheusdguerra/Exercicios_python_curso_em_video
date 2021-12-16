# ex016
# Receba um numero real (float) e mostra apenas a parte interira

from math import floor, trunc

numero_real = float(input('Digite um numero real: '))

print('A parte intera é: {}'.format(floor(numero_real)))
print('A parte intera é: {}'.format(trunc(numero_real)))
print('A parte intera é: {}'.format(int(numero_real)))
