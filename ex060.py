# ex060
# leia um numero qualquer e mostre o seu fatorial

numero = int(input('Digite um número: '))

flag = fatorial = numero

while flag != 1:
    fatorial = fatorial * (numero - 1)
    numero -= 1
    flag -= 1

print(fatorial)
