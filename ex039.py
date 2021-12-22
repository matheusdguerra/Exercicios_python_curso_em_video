# ex039
# receba um ano de nascimento
# informe sobre alistamento militar obrigatório aos 18 anos
from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))

ano_atual = date.today().year

if ano_nascimento + 18 > ano_atual:
    print('Ainda vai se alistar')
elif ano_nascimento + 18 < ano_atual:
    print('Já passou do tempo')
else:
    print('Hora de se alistar')
