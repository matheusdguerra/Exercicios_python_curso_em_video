# ex048
# calcule a soma dos numeros impares que são multiplos de 3 no intervalo de 1 a 500

soma = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            # print(c)
            soma += c

print(soma)
