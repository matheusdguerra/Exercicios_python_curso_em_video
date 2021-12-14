# ex006
# Receba um numero e mostre o dobro, tripo e a raiz quadrada

numero = int(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero**(1/2)

print('O dobro é {}\nO triplo é {}\nA raiz é {:.2f}'.format(dobro, triplo, raiz))
