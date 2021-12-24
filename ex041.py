# ex041
# receba um ano e categorize conforme a idade da pessoa
# até 9 anos -> mirim
# até 14 anos -> infantil
# até 19 anos -> juvenil
# até 20 anos -> sênior
# acima -> master

from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))

ano_atual = date.today().year

if ano_atual - ano_nascimento <= 9:
    print('Mirim')
elif ano_atual - ano_nascimento <= 14:
    print('Infantil')
elif ano_atual - ano_nascimento <= 19:
    print('Junior')
elif ano_atual - ano_nascimento <= 20:
    print('Senior')
else:
    print('Master')
