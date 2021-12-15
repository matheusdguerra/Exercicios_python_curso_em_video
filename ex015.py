# ex015
# receber a quantidade de KM e a quantidade de dias mostre o valor a ser pago
# O aluguel é 60 R$ por dia e 0,15 por km rodado.

distancia_km = float(input('Digite a distancia percorrrida em km: '))
quantidade_dias = float(input('Digite a quantidade de dias: '))

valor_aluguel = (quantidade_dias * 60) + (distancia_km * 0.15)

print('O valor a pagar é: R${}'.format(valor_aluguel))
