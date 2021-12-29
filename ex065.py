# ex064
# receba varios numeros interiros e para apenas quando for digitado 999
# mostre quantos numeros foram digitados e a soma entre eles

flag = 'S'
soma = 0
count = 0

while flag in 'Ss':
    numero = int(input('Digite um numero: '))
    count += 1
    soma += numero
    if count == 1:
        maior = menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

    flag = str(input('Deseja continuar [S/N]'))

print('Média -> {}\nMaior -> {}\nMenor -> {}'.format(soma / count, maior, menor))
