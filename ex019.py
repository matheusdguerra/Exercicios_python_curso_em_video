# ex019
# receba 4 nomes e sorteie um aleatoriamnete.

from random import choice
alunos = []

alunos = input('Digite o nome dos 4 alunos: ').split(" ")

print(alunos)

print('O aluno escolhe é: {}'.format(choice(alunos)))
