# ex096
# crie uma função area() que receba as dimenções de um terreno (largura e comprimento) e mostre a área do terreno

def area(lar, comp):
    area_total = comprimento * largura
    print(f'A área total é {area_total:.2f}m²')


largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))

area(largura, comprimento)
