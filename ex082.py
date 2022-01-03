# ex083
# Leia vários números e coloque em uma lista perguntado se deseja continuar [S/N]
# no final mostre:
# 1 -> uma lista com os valores completos
# 2 -> uma lista com os valores pares
# 3 -> uma lista com os valores impares

lista = []
lista_pares = []
lista_impares = []
cont_digitados = 0


while True:
    # Leitura do numero, teste existe na lista e append
    numero = int(input(f'Digite o {cont_digitados + 1}º valor: '))

    lista.append(numero)

    cont_digitados += 1

    # Controle de saída do programa
    while True:
        flag_saida_input = str(input('Deseja continuar? [S/N]')).upper().strip()
        if flag_saida_input in 'SN':
            break
    if flag_saida_input in 'N':
        break

for c in lista:
    if c % 2 == 0:
        lista_pares.append(c)
    else:
        lista_impares.append(c)

print(f'Lista completa{lista}')
print(f'Lista pares{lista_pares}')
print(f'Lista impares{lista_impares}')
