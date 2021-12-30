# ex066
# Leia vários numerosa inteiros. Parec de pedir qundo o usuário digitar 999
# No final mostre a soma e quantos numeros foram digitados

cont = soma = 0

while True:
    numero = int(input('Digite um número (999 para parar): '))
    if numero == 999:
        break
    cont += 1
    soma += numero

print(f'Foram digitados {cont} e a soma é {soma}')
