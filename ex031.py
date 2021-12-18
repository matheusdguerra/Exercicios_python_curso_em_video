# ex031
# receba a distancia de uma viagem em km
# Calcule o preço da passagem 0,50 R$ por km < 200km e 0,45 para > que 200km

distancia = float(input('Digite a distância: '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('O valor a ser pago é {:.2f} R$'.format(preco))

# if simplificado
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor a ser pago é {:.2f} R$'.format(preco))
