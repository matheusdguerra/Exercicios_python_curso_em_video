# ex102
# crie uma funçaõ que calcule o fatorial recebendo dois parametros.

# fatorial(5, show=True)
# 5 x 4 x 3 x 2 x 1 = 120

# fatorial(5)
# 120

# Help(Fatorial)
# - Calcula o fatorial de um número
# -- Param n: O número a ser calculado
# -- Param show: (opcional) Mostra ou não a conta
# -- return: O valor fatorial de um número n


def fatorial(num=1, show=False):
    '''
    -- Calcula o fatorial de um número
    -- Param num: O número a ser calculado
    -- Param show: (opcional) Mostra ou não a conta
    -- return: O valor fatorial de um número num
    '''

    f = 1  # variavel local
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(f'{c}', end=' = ')
            else:
                print(f'{c}', end=' x ')

    return f  # retorna fatorial e valores no formato lista


help(fatorial)
n = int(input('Digite um numero: '))  # variavel global

print(fatorial(n))  # variavel calculo recebe o retorno do def fatorial
