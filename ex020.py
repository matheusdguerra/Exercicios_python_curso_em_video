# ex020
# recebe 4 nome e apresente a oredem da seleção aleatória

import random
from random import shuffle

alunos = []

alunos = input('Digite o nome de 4 alunos: ').split(" ")

random.shuffle(alunos)

print('Ordem de apresentação: {}'.format(alunos))
