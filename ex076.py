# ex076
# Crie uma listagem de preços em uma tupla com ome  e preço
# ex.: tupla = ('Pão', 1.50, 'Leite', 2.45', 'café' , 7.90)
# No final mostre a listagem dos preços/produtots de forma tabular
# Pão.........R$ 1.50
# Leite.......R$ 2.45
# Café........R$ 7.90
cont = 0
cont_produto = 0
cont_valor = 1
tupla = ('Pão', 150.50, 'Leite', 22.45, 'Café', 7.90, 'Arroz', 15.60, 'Feijão', 7.56, 'Massa', 53.98, 'Tomate', 620.56)

print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)

# for c in range(len(tupla)):
while cont < len(tupla)/2:
    print('{:.<30}R${:7.2f}'.format(tupla[cont_produto], tupla[cont_valor]))
    cont_produto += 2
    cont_valor += 2
    cont += 1

print('-'*40)
