# ex017
# receba o cateto oposto e o cateto adjacente de um triangulo retangulo.
# calcule e mostre o comprimento da hipotenusa

from math import hypot

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)
hipotenusa2 = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print('A hipotenusa é {:.2f}'.format(hipotenusa))
print('A hipotenusa é {:.2f}'.format(hipotenusa2))
