# ex022
# receba um nome completo e mostre os itens abaixo.
# -> nome com todas as letras maiusculas
# -> nome com todas as letras minusculas
# -> Quantas letras tem o nome sem contar espaços
# -> Quantas letras tem o primeiro nome

nome = input('Digite um nome completo: ').strip()

print(nome)
print('Nome maiusculo: {}'.format(nome.upper()))
print('Nome minusculo: {}'.format(nome.lower()))
print('Quantidade de letras sem espaço: {}'.format(len(nome.replace(' ', ''))))
print('Quantidade de letras sem espaço: {}'.format(len(nome) - nome.count(' ')))

nome = nome.split()
print('O primeiro nome {} tem {} letras'.format(nome[0], len(nome[0])))
