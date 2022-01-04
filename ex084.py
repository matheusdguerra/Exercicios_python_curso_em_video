# ex084
# Leia nome e peso de várias pessoas guardando em uma lista
# No final mostre
# -> Quantas pessoas foram cadastradas
# -> Listagem das pessoas mais pesadas
# -> Listagem das pessoas mais leves

nomes_pesados = []
nomes_leves = []
lista = []
lista_temp = []
cont_digitados = quantidade_digitados = 0


while True:
    # Leitura do numero, teste existe na lista e append
    lista_temp.append(str(input(f'Digite o {cont_digitados + 1}º nome: ')))
    lista_temp.append(int(input(f'Digite o {cont_digitados + 1}º peso: ')))
    lista.append(lista_temp[:])
    lista_temp.clear()

    cont_digitados += 1

    # Controle de saída do programa
    while True:
        flag_saida_input = str(input('Deseja continuar? [S/N]')).upper().strip()
        if flag_saida_input in 'SN':
            break
    if flag_saida_input in 'N':
        break

print(lista)

for c in lista:
    if quantidade_digitados == 0:
        maior_peso = c[1]
        menor_peso = c[1]
    else:
        if c[1] >= maior_peso:
            maior_peso = c[1]
        if c[1] <= menor_peso:
            menor_peso = c[1]

    quantidade_digitados += 1

for c in lista:
    if c[1] == menor_peso:
        nomes_leves.append(c[0])
    if c[1] == maior_peso:
        nomes_pesados.append(c[0])

print(f'A quantidade de cadastros digitados foi {quantidade_digitados}')
print(f'O maior peso foi {maior_peso} e são {nomes_pesados}')
print(f'O menor peso foi {menor_peso} e são {nomes_leves}')
