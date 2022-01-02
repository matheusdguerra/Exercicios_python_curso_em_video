# ex079
# receba vaários valores e cadastreos em uma lista.
# Pergunte s eo usuário desej adigitar um novo valor [S/N]
# caso o núemro já exista na lista ele não deve ser adicionado
# no final mostrs os valores únicos digitados em ordem crescente

lista = []
cont_digitados = 0
cont_num_unicos = 0


while True:
    # Leitura do numero, teste existe na lista e append
    numero = int(input(f'Digite o {cont_digitados + 1}º valor: '))
    if numero not in lista:
        lista.append(numero)
        cont_num_unicos += 1
    else:
        print(f'O numero {numero} já está na lista')

    cont_digitados += 1

    # Controle de saída do programa
    while True:
        flag_saida_input = str(input('Deseja continuar? [S/N]')).upper().strip()
        if flag_saida_input in 'SN':
            break
    if flag_saida_input in 'N':
        break

lista.sort()

print(f'Foram digitados {cont_num_unicos} numeros unicos\nOs números digitados foram {lista}')
