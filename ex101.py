# ex101
# crie uym função que calcule a idade da pessoa pela data de nascimento e informe litralmente o status para votação

# -> 18 anos -> VOTO OBRIGATORIO
# -> 8 anos ->  NAO VOTA
# -> 48 -> VOTO OBRIGATORIO
# -> 108 anos -> VOTO OPCIONAL


def calcula_idade(dt):
    from datetime import date, datetime

    ano_atual = date.today().year
    idade = ano_atual - dt

    if idade < 16:
        return(f'Com {idade} anos: NÃO VOTA')
    elif 16 <= idade < 18 or idade > 65:
        return(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        return(f'Com {idade} anos: VOTO OBRIGATÓRIO')


data_nascimento = (int(input('Digite o ano de nascimento: ')))
print(calcula_idade(data_nascimento))
