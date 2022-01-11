# ex101
# crie uym função que calcule a idade da pessoa pela data de nascimento e informe litralmente o status para votação

# -> 18 anos -> VOTO OBRIGATORIO
# -> 8 anos ->  NAO VOTA
# -> 48 -> VOTO OBRIGATORIO
# -> 108 anos -> VOTO OPCIONAL

from datetime import date, datetime


def calcula_idade(dt):
    if idade < 15:
        return('NÃO VOTA')
    elif idade > 16 and idade < 65:
        return('VOTO OBRIGATÓRIO')
    elif idade > 65:
        return('VOTO OPCIONAL')


data_nascimento = int(input('Digite o ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - data_nascimento

print(f'Com {idade} anos: {calcula_idade(data_nascimento)}')
