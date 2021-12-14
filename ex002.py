# entrada e saida de dados
import sys

# Ex02
# Receba um nome e imprima com a mensagem 'Bem-vindo' e o nome recebido

# por padrão o input lê string
nome = input('Digite seu nome: ')
print('Bem-vindo', nome)
print('Bem-vindo {}!'.format(nome))

dia = input('Digite o dia de nascimento: ')
mes = input('digite o mes de nascimento: ')
ano = input('Digite o ano de nascimento: ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto?')

# input de inteiros
print('Digite sua idade e seu peso:')
idade, peso = map(int, sys.stdin.readline().split())
print(nome, 'sua idade é', idade, 'seu peso é', peso)

# input de arquivo txt
arquivo = open('input_txt.txt', 'r', encoding='utf8')
conteudo = arquivo.read()
print(conteudo)

for linha in arquivo.readlines():
    print(linha)
