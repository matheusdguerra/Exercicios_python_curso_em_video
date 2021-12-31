# Variaveis compostas (TUPLAS)
# Tupals são imutáveis

from typing import Counter


lanche = ('Xis', 'Suco', 'Pizza', 'Pudim')
print(len(lanche))

print(lanche[1])
print(lanche[-1])
print(lanche[1:3])
print(lanche[0:])

for c in lanche:
    print(c)

for c in range(0, len(lanche)):
    print(lanche[c])

for posicao, c in enumerate(lanche):
    print(posicao, c)

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = (a + b)  # (2, 5, 4, 5, 8, 1, 2)
print(c)
print(len(c))  # 7
print(c.count(5))  # 2
print(c.index(8))  # 4
print(c.index(4))  # 2
print(c.index(2))  # 0
print(c.index(2, 4))  # 6

pessoa = ('Matheus', 32, 'M', 63.85)
print(pessoa)

del(pessoa)
