# ex103
# Monte uma função que receba dois parametros opcionais (nome=<desconhecido> e gols=0)
# se for digitado uma string no gol o parametro deve receber 0
# mostre na tela o nome os gols do jogador.

def ficha(n='<Desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols no campeonato.')


nome = str(input('Nome: '))
gols = str(input('Gols: '))

# Trata variavel gols para int
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

# Trata variavel nome
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
