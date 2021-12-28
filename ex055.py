# ex055
# Leia 5 pesos e diga qual o maior e o menor peso

pesos = []

for c in range(0, 5):
    peso = float(input('Digite o {}º peso: '.format(c + 1)))
    pesos.append(peso)

maior = pesos[0]
menor = pesos[0]

for c in pesos:
    if c > maior:
        maior = c
    if c < menor:
        menor = c

print('O maior peso é {}Kg'.format(maior))
print('O menor peso é {}Kg'.format(menor))
