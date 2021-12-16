# ex018
# receba um ânmgulo e mostre cosseno e tangente

from math import cos, tan, sin, radians

angulo = float(input('Digite um angulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O seno é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}'.format(seno, cosseno, tangente))
