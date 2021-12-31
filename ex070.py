# ex070
# Leia nome e preço de vários produtos
# O programa deve eprguntar se deseja continuar.
# No fInal mostre:
# -> Qual o total gasto na compra
# -> quando produto custam mais de 1000 reais
# -> qual o nome do produto mais barato

total_gasto = cont = maiores_1000 = 0

while True:

    produto = str(input('Digite um produto: '))
    preco = float(input('Digite o valor: '))

    total_gasto += preco

    if preco > 999:
        maiores_1000 += 1

    if cont == 0 or preco_produto_barato > preco:
        nome_produto_barato = produto
        preco_produto_barato = preco

    cont += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break

print(f'Total gasto: {total_gasto:.2f}R$')
print(f'Quantidade de produtos maiores de 1000.00 R$: {maiores_1000}')
print(f'Produto mais barato: {nome_produto_barato}')
