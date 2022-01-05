# ex089
# Leia nome e duas notas guarde em listas compostas
# [[nome], [nota1, nota2], [media]]

cont_alunos_digitados = 0
soma_media = count = 0
lista = [[], [[], []], []]

while True:
    lista[0].append(str(input(f'Digite o {cont_alunos_digitados + 1}º nome: ')))
    for c in range(0, 2):
        lista[1][c].append(float(input(f'Digite a {c + 1}º nota: ')))
    cont_alunos_digitados += 1

    # Controle de saída do programa
    while True:
        flag_saida_input = str(input('Deseja continuar? [S/N]')).upper().strip()
        if flag_saida_input in 'SN':
            break
    if flag_saida_input in 'N':
        break

# processamento da média
for c in range(0, cont_alunos_digitados):
    soma_media = lista[1][0][c]+lista[1][1][c]
    lista[2].append(soma_media/2)

# saída das informações
print('=-' * 30)
print('No.   Nome        Média')
for c in range(0, cont_alunos_digitados):
    print(f'{c:<5} {lista[0][c]:<6} {lista[2][c]:>10.1f}')

# mostrar notas em detalhes
while True:
    no = int(input(f'Digite o codigo do aluno [999 para sair]: '))
    # Controle de saída do programa

    if no == 999:
        break

    # saída do resultado
    if no < (len(lista[0])):
        print(lista[1][0][no], lista[1][1][no])
    else:
        print('Codigo aluno inválido')
