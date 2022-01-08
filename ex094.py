# ex094
# leia nome, sexo e idade de várias pessoas
# guarde cada pessoa em um dicionário e todos os dicionários em uma lista
# no final mostre
# -> Quantas pessoas foram cadastradas
# -> A media de idade do grupo
# -> Uma lista com todas as mulheres
# -> Uma lista com todas as pessoas com idade acima da media

lista_pessoas = []
lista_mulheres = []
lista_pessoas_acima_media = []
biblioteca_pessoa = {}
soma_idade = 0

while True:
    # Leitura do numero, teste existe na lista e append
    # biblioteca_pessoa.clear() # com ou sem o clear() ocorre a mesma situação
    biblioteca_pessoa['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo [M/F]: '))
        if sexo in ('MmFf'):
            biblioteca_pessoa['sexo'] = sexo.lower()
            break
        else:
            print('Digite um sexo válido [M/F]')

    biblioteca_pessoa['idade'] = int(input('Idade: '))

    print('=-' * 30)

    lista_pessoas.append(biblioteca_pessoa.copy())

    # Controle de saída do programa
    while True:
        flag_saida_input = str(input('Deseja continuar? [S/N]')).upper().strip()
        if flag_saida_input in 'SN':
            break
        else:
            print('Digite apenas [S ou N]')
    if flag_saida_input in 'N':
        break

# Processamento dos dados

for c in range(0, len(lista_pessoas)):
    soma_idade += lista_pessoas[c]['idade']

media_idades = soma_idade / len(lista_pessoas)

for c in range(0, len(lista_pessoas)):
    #soma_idade += lista_pessoas[c]['idade']

    if lista_pessoas[c]['sexo'] == 'f':
        lista_mulheres.append(lista_pessoas[c]['nome'])

    if lista_pessoas[c]['idade'] > media_idades:
        lista_pessoas_acima_media.append(lista_pessoas[c])

# Saída dos dados
print('=-' * 60)
print(f'Lista total\n {lista_pessoas}')
print('=-' * 60)

print(f'Foram cadastradas {len(lista_pessoas)} pessoas')
print(f'Media das idades {media_idades:.2f}')
print(f'A lista de mulheres é:', end=' ')
for c in lista_mulheres:
    print(c, end=' ')

print('\nLista de pessoas com idade acima da média é: ')
for c in lista_pessoas_acima_media:
    print(f'nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}')
    print()
