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
    - Calcula o fatorial de um número
    -- Param num: O número a ser calculado
    -- Param show: (opcional) Mostra ou não a conta
    -- return: O valor fatorial de um número num
    '''

    lista_conta.clear()
    f = 1  # variavel local
    for c in range(num, 0, -1):
        f *= c
        if show:
            lista_conta.append(c)
    return [f, lista_conta]  # retorna fatorial e valores no formato lista


lista_conta = []

help(fatorial)
n = int(input('Digite um numero: '))  # variavel global

calculo = fatorial(2, True)  # variavel calculo recebe o retorno do def fatorial


for c in calculo[1]:
    if c == 1:
        print(f'{c}', end=' = ')
    else:
        print(f'{c}', end=' x ')

print(f'{calculo[0]}')

# print(f'Fatrinal de {n} é {fatorial(n,True)}')
