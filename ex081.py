# ex081
# Leia vários números e coloque em uma lista perguntado se deseja continuar [S/N]
# no final mostre:
# 1 -> quantos numeros foram digitados
# 2 -> A lista em orfem decrescente
# 3 -> Se o valor 5 foi digitado e se está na lista ou não

lista = []
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

print(f'Forma digitados {cont_digitados} números')
lista.sort(reverse=True)
print(f'Ordem decrescente{lista}')
print(f'Tem 5 na posição {lista.index(5) + 1}' if 5 in lista else 'Não tem 5')
