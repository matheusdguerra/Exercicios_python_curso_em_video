# ex030
# receba um numero inteiro e mostre se é par ou impar

from random import randint, sample
# numero = int(input('Digite um número: '))
# numero = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numero = [randint(0, 99)]

# lista_rondamica = []
# for n in range(0, 30):
#    lista_rondamica.append(randint(0, 100))

lista_rondamica = sample(range(0, 1000), 10)

for n in lista_rondamica:
    if n % 2 == 0:
        print('{} É par!'.format(n))
    else:
        print('{} É impar!'.format(n))
