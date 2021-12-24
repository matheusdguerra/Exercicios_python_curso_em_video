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

idade = ano_atual - ano_nascimento

if ano_atual - ano_nascimento <= 9:
    print('{} Anos -> Mirim'.format(idade))
elif ano_atual - ano_nascimento <= 14:
    print('{} Anos -> Infantil'.format(idade))
elif ano_atual - ano_nascimento <= 19:
    print('{} Anos -> Junior'.format(idade))
elif ano_atual - ano_nascimento <= 20:
    print('{} Anos -> Senior'.format(idade))
else:
    print('{} Anos -> Master'.format(idade))
