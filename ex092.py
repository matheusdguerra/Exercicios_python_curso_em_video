# ex093
# Leia nome, ano de nascimento e numero carteira de trabalho
# Cadastre com a idade e não o ano de nascimento em um dicionário
# se carteira de trabalho for diferente de 0 pedir tambem o ano de cotratação e o salário
# calcule também com quantos anos a pessoa vai se aposentar (35 anos de contribuição)

from datetime import date

# Entrada dos dados
ctps = {}

ctps['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
ctps['carteira_trabalho'] = int(input('Carteira de trabalho (0 não tem): '))

if ctps['carteira_trabalho'] != 0:
    ctps['ano_contratacao'] = int(input('Ano contratação: '))
    ctps['salario'] = float(input('Salário: R$ '))


# Processamento das informações

ano = date.today().year
ctps['idade'] = ano - ano_nascimento
if ctps['carteira_trabalho'] != 0:
    ctps['anos_aposentadoria'] = (ctps['ano_contratacao'] + 35) - ano_nascimento


# Saída das informações
print(ctps)
print()
print(f'    - Nome => {ctps["nome"]}')
print(f'    - Idade => {ctps["idade"]}')
print(f'    - CTPS => {ctps["carteira_trabalho"]}')
if ctps['carteira_trabalho'] != 0:
    print(f'    - Ano contratação => {ctps["ano_contratacao"]}')
    print(f'    - Salário => {ctps["salario"]}')
    print(f'    - Aposentadoria => {ctps["anos_aposentadoria"]}')
