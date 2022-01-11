# =======================
# --->  Interactive Help
# =======================
help()

help(print)

print(print.__doc__)

# ==========================
# ---> docstring
# ==========================

# Documentação de funções do usuário
# def contador(i, f, p)
#     contador(2, 10, 2)


def contador(i, f, p):
    """
    i -> iniio da contagem
    f -> fim da contagem
    p -> passo da contagem
    return -> sem retorno
    """
    pass


help(contador)


# ==========================
# ---> Argumentos opcionais
# ==========================


def soma(a=0, b=0, c=0):
    """
    soma a + b + c em s
    imprimi s na tela
    parametros a b e c com 0 por padrão
    """
    s = a + b + c
    print(s)


soma(3, 4, 6)
soma(1, 8)
soma()
soma(b=4, c=6)

# =========================
# ---> Escopo de variáveis
# =========================


def teste(b):
    b += 4  # variavel local
    c = 2  # variavel local
    print(f'A dentro vale {a}: ')  # 5
    print(f'B dentro vale {b}: ')  # 9
    print(f'C dentro vale {c}: ')  # 2


a = 5  # variavel global
teste(a)
print(f'A fora vale {a}: ')  # 5
# print(f'B fora vale {b}: ')  # ERRO
# print(f'C fora vale {c}: ')  # ERRO
# --------------------------------------------------------------------


def teste2(b):
    a = 4  # variavel local
    b += 4  # variavel local
    c = 2  # variavel local
    print(f'A dentro vale {a}: ')  # 4
    print(f'B dentro vale {b}: ')  # 9
    print(f'C dentro vale {c}: ')  # 2


a = 5  # variavel global
teste(a)
print(f'A fora vale {a}: ')  # 5
# print(f'B fora vale {b}: ')  # ERRO
# print(f'C fora vale {c}: ')  # ERRO

# --------------------------------------------------------------------


def teste3(b):
    global a
    a = 8  # variavel local
    b += 4  # variavel local
    c = 2  # variavel local
    print(f'A dentro vale {a}: ')  # 4
    print(f'B dentro vale {b}: ')  # 9
    print(f'C dentro vale {c}: ')  # 2


a = 5  # variavel global
teste(a)
print(f'A fora vale {a}: ')  # 8
# print(f'B fora vale {b}: ')  # ERRO
# print(f'C fora vale {c}: ')  # ERRO

# ===========================
# ---> Retorno de resultados
# ===========================


def soma(a=0, b=0, c=0):

    s = a + b + c
    return(s)


print(soma(1, 2, 3))
resp = soma(3, 4, 6)
print(resp)
resp2 = soma(1, 8)
resp3 = soma(4)
print(f'Os resultados foram {resp2}, {resp3}')

# ------------------------------------------------------


def fatorial(num=1):
    f = 1  # variavel local
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um numero: '))  # variavel global
print(f'Fatrinal de {n} é {fatorial(n)}')

f1 = fatorial(4)
f2 = fatorial(5)
f3 = fatorial()
print(f'Os resoltados são {f1} {f2} {f3}')

# ------------------------------------------------------

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(par(num))

if par(num):
    print('É par')
else:
    print('é impar')
