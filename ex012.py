# ex012
# receba um preco e mostre o novo preco com 5% de descontro

preco_original = float(input('Digite um preço: '))

novo_preco = preco_original - (preco_original * 0.05)

print('Novo preço é {}'.format(novo_preco))
