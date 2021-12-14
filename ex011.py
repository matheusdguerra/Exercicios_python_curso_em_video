# ex011
# receba a largura e altura e calcule a área
# também calcule a quantidade de tinta para pint-lá
# cada litro de tinta pinta 2m²

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

area = largura * altura
litros = area / 2

print('A área é {}'.format(area))
print('A quantidade de litros é {}'.format(litros))
