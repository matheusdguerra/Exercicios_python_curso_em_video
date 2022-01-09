# ex098
# crie uma função contator() que recebe 3 parâmetros (inicio, fim e passo)
# -> conte de 1 até 10, de 1 em 1
# -> de 10 até 0, de 2 em 2
# -> contagem personalizada, recebendo inico fim e passo


# Inicio: 90
# Fim: 40
# Passo: 10
#
# Inicio: 20
# Fim: 10
# Passo: -1 -> +1 Se passo for passado negativo tranforma em positivo
#
# Inicio: 5
# Fim: -5
# Passo: 0 -> +1 Se passo for 0 tranforma em 1

from time import sleep

lista_contador = []


def contador(i, f, p):
    if f < i:
        if p < 0:
            for c in range(i, f-1, p):
                lista_contador.append(c)
        elif p == 0:
            for c in range(i, f-1, -1):
                lista_contador.append(c)
        elif p > 0:
            p = (p * -1)
            for c in range(i, f-1, p):
                lista_contador.append(c)
    else:
        if p == 0:
            p = 1
        for c in range(i, f+1, p):
            lista_contador.append(c)

    for c in lista_contador:
        print(c, end=' ')
    print('Fim!')


print('=-'*25)
print('Contagem de 1 até 10, de 1 em 1')
for c in range(1, 11):
    print(c, end=' ', flush=True)
    sleep(0.3)
print('Fim!')

print('=-'*25)
print('Contagem de 10 até 0, de 2 em 1')
for c in range(10, -1, -1):
    print(c, end=' ', flush=True)
    sleep(0.3)
print('Fim!')


print('=-'*25)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
