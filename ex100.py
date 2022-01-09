# ex100
# crie uma lista chamada numeros[] e  duas funções sorteia() e somapar()
# a função sorteia() vai sortear 5 números e colocar dentro da lista numeros[]
# a função somapar() vai somar os pares sorteados pela função anterior

from random import sample
from time import sleep


def sorteia():
    lista_numeros = (sample(range(1, 15), 6))
    print('Sorteando os números', end=' ')
    for c in lista_numeros:
        print(f'{c}', end=' ', flush=True)
        sleep(0.3)
    return(lista_numeros)


def somapar(lista):
    s = 0
    for c in lista:
        if c % 2 == 0:
            s += c
    print(f'\nA soma dos pares da lista {lista} é: {s}')


n = sorteia()

somapar(n)
