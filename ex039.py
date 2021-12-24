# ex039
# receba um ano de nascimento
# informe sobre alistamento militar obrigatório aos 18 anos
from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))

ano_atual = date.today().year

if ano_nascimento + 18 > ano_atual:
    print('Ainda vai se alistar')
    print('Faltam {} anos'.format(18 - (ano_atual - ano_nascimento)))
elif ano_nascimento + 18 < ano_atual:
    print('Já passou do tempo')
    print('Passaram {} anos'.format(ano_atual - (ano_nascimento + 18)))
else:
    print('Hora de se alistar')
