# ex099
# crie uma função maior() que receba vários parametros com valores inteiros
# A funçaõ deve analisar todos os valores e diser qual o maior

from random import sample
from time import sleep


def maior(*numeros):
    if numeros != ():
        for idx, c in enumerate(numeros[0]):
            print(c, end=' ', flush=True)
            sleep(0.3)
            if idx == 0:
                max = c
            else:
                if c > max:
                    max = c
        print(f'Foram passados {len(numeros[0])} números')
        print(f'O maior número é: {max}')
        print('=-' * 20)
    else:
        print(f'Você informou 0 valor')


maior(sample(range(1, 30), 6))
maior(sample(range(1, 30), 4))
maior(sample(range(1, 30), 1))
maior()
