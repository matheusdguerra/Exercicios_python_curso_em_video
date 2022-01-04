# ex089
# Leia nome e duas notas guarde em listas compstas

#[[nome], [nota1, nota2], [media]]

cont_alunos_digitados = 0
cont_notas_digitadas = 0
lista = []
lista_temp = []

while True:
    # Leitura do numero, teste existe na lista e append
    lista_temp.append(str(input(f'Digite o {cont_alunos_digitados + 1}º nome: ')))
    for c in range(0, 2):
        lista_temp.append(str(input(f'Digite a {cont_notas_digitadas + 1}º nota: ')))
    lista.append(lista_temp[:])
    lista_temp.clear()

    cont_alunos_digitados += 1

    # Controle de saída do programa
    while True:
        flag_saida_input = str(input('Deseja continuar? [S/N]')).upper().strip()
        if flag_saida_input in 'SN':
            break
    if flag_saida_input in 'N':
        break

print(lista)
