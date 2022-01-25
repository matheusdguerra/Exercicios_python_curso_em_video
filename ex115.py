# ex115
# crie um sistema modularizado que cadastre nome e idade e salve em um arquivo de texto
# o sistema via ter duas opções. Cadastras e listas as pessoas cadastradas
# Tratar exeções
# criar arquivos txt caso não exista


# Menu
# 1 lista
# 2 adiciona
# 3 sai do sistema


from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])

    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Sainda do sistema... Até logo!')
        break
    else:
        print('\033[31mErro: Digite uma opção válida\033[m')
    sleep(1)
