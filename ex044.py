# ex044
# receba um valor e a condição de pagamento

# 1 -> À vista em dinheiro ou cheque 10% de desconto
# 2 -> Á vista no cartão 5% de desconto
# 3 -> em até 2x no cartão preço normal
# 4 -> em 3x ou mais no cartão 20% de juros

preco = float(input('Digite o preço: '))
condicao = int(input('Digite a condição: '))


if condicao == 1:
    preco = preco - (preco * 0.10)
    print('Novo valor com 10% de desconto {}'.format(preco))
elif condicao == 2:
    preco = preco - (preco * 0.05)
    print('Novo valor com 5% de desconto {}'.format(preco))
elif condicao == 3:
    preco = preco
    print('valor normal {}'.format(preco))
elif condicao == 4:
    preco = preco + (preco * 0.20)
    print('Novo valor com 20% de juros {}'.format(preco))
