# Rotinas
# toda a função tem parenteses

# Funções que vem com o python
# print()
# len()
# input()
# int()
# float()

# Funções criadas pelo usuário

# mostrarlinha()
# =-=-=-=-=-=-=-=-=-=-=-
# CADASTRO
# =-=-=-=-=-=-=-=-=-=-=-

def mostralinha():
    print('=-' * 10)


def mostralinha2(mensagem):
    print('=-' * 10)
    print(mensagem)
    print('=-' * 10)


mostralinha()
print('TESTE')
mostralinha()

mostralinha2('TESTE')
mostralinha2('PROGRAMAÇÃO')


# --------------------------------------------
def soma(a, b):
    s = a + b
    print(f'A = {a} B = {b} A soma é {s}')


a = 4
b = 5
s = a + b
print(s)
soma(4, 5)
soma(1, 2)
soma(a=8, b=2)
soma(b=1, a=4)


# Recurso de descomapctar quando não se sabe a quantidade de parâmetros
def contador(* num):
    tamanho = len(num)
    print(tamanho)
    for i in num:
        print(i, end=' ')
    print()


contador(5, 7, 3, 1, 4)
contador(3, 1, 4)
contador(4)

# ---------------------------------------------------------------


def dobra_valores(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    print(valores)


valores = [7, 2, 5, 0, 4]
dobra_valores(valores)
