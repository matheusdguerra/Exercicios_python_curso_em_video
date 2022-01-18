def metade(n=0, f=False):
    if f:       # Primeira maneira de fazer o teste do parâmetro f
        n = moeda(n / 2)
    else:
        n = n / 2
    return n


def dobro(n=0, f=False):
    n = n * 2
    return n if f is False else moeda(n)  # Segunda maneira de fazer o teste do parâmetro f


def aumentar(n=0, p=0, f=False):
    if f:
        n = moeda(n + (n * p / 100))
    else:
        n = n + (n * p / 100)
    return n


def diminuir(n=0, p=0, f=False):
    if f:
        n = moeda(n - (n * p / 100))
    else:
        n = n - (n * p / 100)
    return n


def moeda(n=0, moeda='R$', f=False):
    n = f'{moeda}{n:>.2f}'.replace('.', ',')
    return n


def resumo(p, a=10, d=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Analisando {moeda(p)}')
    print('-'*30)
    print(f'Metade do preço..: \t{metade(p, True)}')
    print(f'Dobro do preço...: \t{dobro(p,True)}')
    print(f'Aumentado {a}%....: \t{aumentar(p, a, True)}')
    print(f'diminuindo {d}%...: \t{diminuir(p, d, True)}')
