# ex010
# Receba um valor em reais e converta em dolar
# receba um valor em reis e mostre quando dolares é possível comprar
# 1 dolar = 3.23 reais

dolar = 3.27

valor_reais = float(input('Digite um valor em reais: '))

valor_dolar = dolar * valor_reais
print('O valor {} em reais convertido em dolar é {:.2f} '.format(valor_reais, valor_dolar))

comprar_dolar = valor_reais / dolar
print('Você pode comprar {:.2f} dolares'.format(comprar_dolar))
