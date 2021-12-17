# ex027
# Receba um nome completo e mostre separadamento o primeio e o ultimo nome

nome = input('Digite um nome completo: ')
nome = nome.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome: {}'.format(nome[-1]))
