# ex044
# receba um valor e a condição de pagamento

# 1 -> À vista em dinheiro ou cheque 10% de desconto
# 2 -> Á vista no cartão 5% de desconto
# 3 -> em até 2x no cartão preço normal
# 4 -> em 3x ou mais no cartão 20% de juros

preco = float(input('Digite o preço: '))

print('''
# 1 -> À vista em dinheiro ou cheque 10% de desconto
# 2 -> Á vista no cartão 5% de desconto
# 3 -> Em até 2x no cartão preço normal
# 4 -> Em 3x ou mais no cartão 20% de juros
''')

condicao = int(input('Digite a condição: '))


if condicao == 1:
    preco = preco - (preco * 0.10)
    print('Novo valor com 10% de desconto {:.2f}'.format(preco))
elif condicao == 2:
    preco = preco - (preco * 0.05)
    print('Novo valor com 5% de desconto {:.2f}'.format(preco))
elif condicao == 3:
    preco = preco
    valor_parcelas = preco / 2
    print('valor normal {:.2f}'.format(preco))
    print('Parcela em 2x de {:.2f}'.format(valor_parcelas))
elif condicao == 4:
    parcelas = int(input('Quantas parcelas: '))
    novo_preco = preco + (preco * 0.20)
    valor_parcelas = novo_preco / parcelas
    print('Novo valor com 20% de juros {:.2f}'.format(novo_preco))
    print('Valor das parcelas {:.2f}'.format(valor_parcelas))
else:
    print('Condição inválida')
