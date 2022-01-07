# ex093
# Leia nome de um jogador de futebol  quantidade de partidas
# Depois quantidade de gols de cada partida
# Guarde tudo em um dicionário

cadastro_jogador = {}
lista_gols = []
totgols = 0

cadastro_jogador['nome'] = str(input('Nome: '))
quantidade_jogos = int(input('Quantidade de jogos: '))


# if quantidade_jogos != 0:
for c in range(0, quantidade_jogos):
    gols = int(input(f'Gols da {c+1}ª partida: '))
    lista_gols.append(gols)
    totgols += gols

cadastro_jogador['gols_por_partida'] = lista_gols
cadastro_jogador['total_gols'] = totgols

# Saída de dados
print('=-'*30)
print(cadastro_jogador)
print('=-'*30)
print(f'O campo nome tem o valor {cadastro_jogador["nome"]}')
print(f'O campo gols por partida tem o valor {cadastro_jogador["gols_por_partida"]}')
print(f'O campo gols tem o valor {cadastro_jogador["total_gols"]}')
print('=-'*30)

print(f'O jogados {cadastro_jogador["nome"]} jogou {quantidade_jogos} partidas')
for idx, c in enumerate(lista_gols):
    print(f' => Na partida {idx+1}, fez {c} gols')
