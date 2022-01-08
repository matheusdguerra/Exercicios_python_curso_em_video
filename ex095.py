# ex095
# Leia nome de varios jogadores de futebol e quantidade de partidas
# Depois leia s quantidade de gols de cada partida
# Guarde tudo em um dicionário
# No final mostre um visualização de aproveitamento

lista_detalhada_jogador = []
cadastro_jogador = {}
lista_gols = []
totgols = 0

while True:
    cadastro_jogador['nome'] = str(input('Nome: '))
    quantidade_jogos = int(input('Quantidade de jogos: '))

    # if quantidade_jogos != 0:
    for c in range(0, quantidade_jogos):
        gols = int(input(f'Gols da {c+1}ª partida: '))
        lista_gols.append(gols)
        totgols += gols

    cadastro_jogador['gols_por_partida'] = lista_gols[:]
    cadastro_jogador['total_gols'] = totgols

    lista_detalhada_jogador.append(cadastro_jogador.copy())

    lista_gols.clear()
    totgols = 0

    # Controle de saída do programa
    while True:
        flag_saida_input = str(input('Deseja continuar? [S/N]')).upper().strip()
        if flag_saida_input in 'SN':
            break
    if flag_saida_input in 'N':
        break

# Saída de dados
print('=-' * 50)
# print(f'{"No.":<4}{"NOME":<10}{"GOLS":<18}{"TOTAL GOLS":<8}')
print('Cod ', end='')
for i in cadastro_jogador.keys():
    print(f'{i:<19}', end='')
print()

print('-' * 50)
for idx, c in enumerate(lista_detalhada_jogador):
    print(f'{idx:<3}{c["nome"]:<20}{str(c["gols_por_partida"]):<19}{c["total_gols"]:<19}')
print('-' * 50)


# mostrar notas em detalhes
while True:
    no = int(input(f'Digite o codigo do jogador [999 para sair]: '))
    # Controle de saída do programa

    if no == 999:
        break

    # saída do resultado
    if no < (len(lista_detalhada_jogador)):
        print(f'DETALHAMNETO DO JOGADOR {lista_detalhada_jogador[no]["nome"]}')
        # print(lista_detalhada_jogador[no])
        for k, c in enumerate(lista_detalhada_jogador[no]["gols_por_partida"]):
            print(f'No jogo {k+1} fez {c} gols.')
    else:
        print('Codigo aluno inválido')
