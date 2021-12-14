# ex006
# Receba um número e mostre o dobro, tripo e a raiz quadrada

numero = int(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero**(1/2)

print('O dobro é {}\nO triplo é {}\nA raiz é {:.2f}'.format(dobro, triplo, raiz))
print('A Raiz de {} é {:.2f}'.format(numero, pow(numero, 1/2)))
