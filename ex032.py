# ex032
# Receba uma no e mostre se é bissexto

from calendar import isleap
from datetime import date

ano = int(input('Digite um ano qualquer: '))
if ano == 0:
    ano = date.today().year

# Anos bissextos são aqueles que são múltiplos de 4, como 1996, 2000, 2004 etc (que podem ser divididos por 4 deixando resto 0).
# Porém, há uma exceção: múltiplos de 100 que não sejam múltiplos de 400.

# Uma das duas condições a seguir deve ser verdadeira:
# Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
# Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)

print(ano % 4 == 0)
print(ano % 100 != 0)
print(ano % 400 == 0)

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('{} é bissexto'.format(ano))
else:
    print('{} não é bissexto'.format(ano))

# Resolvendo com função
if isleap(ano):
    print('{} é bissexto'.format(ano))
else:
    print('{} não é bissexto'.format(ano))
