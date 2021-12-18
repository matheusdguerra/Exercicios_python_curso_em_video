# ex036
# receba 3 comprimentos e diga se é pssivel fazer um triangulo
from random import sample

ld = sample(range(0, 100), 3)

if ld[0] < (ld[1] + ld[2]) and ld[1] < (ld[0] + ld[2]) and ld[2] < (ld[0] + ld[1]):
    print('Pode formar triângulo')
else:
    print('Não pode formar triângulo')

if ld[0] > ld[1] and ld[0] > ld[2]:
    maior_numero = ld[0]
    sobras = ld[1], ld[2]
elif ld[1] > ld[2]:
    maior_numero = ld[1]
    sobras = ld[0], ld[2]
else:
    maior_numero = ld[2]
    sobras = ld[0], ld[1]


if maior_numero < (sobras[0] + sobras[1]):
    print('É possível fazer um triângulo')
else:
    print('Não é possível fazer um triângulo')

print(ld)
print(maior_numero)
print(sobras)
