# criei um modulo que tenha as funções aumentar(), dominuir() dobro() metade()
# faça um programa que importe e use esses modulos

from ex107_modulo import aumentar, diminuir, metade, dobro

p = float(input('Digite um preço: R$'))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentado 10% {p} é {aumentar(p, 0.10)}')
print(f'diminuindo 13% {p} é {diminuir(p, 0.13)}')
