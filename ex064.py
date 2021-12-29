# ex064
# receba varios numeros interiros e para apenas quando for digitado 999
# mostre quantos numeros foram digitados e a soma entre eles

count = 0
soma = 0
numero = 0
numero = int(input('Digite um numero: '))
while numero != 999:
    # numero = int(input('Digite um numero: '))
    count += 1
    soma += numero
    numero = int(input('Digite um numero: '))
print('Foram digitados {} numeros e a soma é {}.'.format(count, soma))
