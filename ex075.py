# ex075
# Receba 4 valores e guarde-os em uma tupla
# Mostre:
# 1 -> Quantas vezes apareceu o número 9
# 2 -> Em que posição foi digitado o valor 3
# 3 -> Quais foram os números pares.

cout_input = 0
cout_pos_tupla = 0
tupla = ()
cont_9 = 0
flag_pos_3 = True
pos_3_final = 0
tupla_numeros_pares = ()

while cout_input != 4:
    cout_input += 1
    numero = tuple(input('Digite um número: '))
    tupla = tupla + numero

for c in tupla:

    if c == '9':
        cont_9 += 1

    if flag_pos_3 is True and int(c) == 3:
        pos_3_final = cout_pos_tupla
        flag_pos_3 = False

    if int(c) % 2 == 0:
        tupla_numeros_pares = tupla_numeros_pares + tuple(c)

    cout_pos_tupla += 1

print(f'Números digitados: {tupla}')
print(f'Quantidade de 9: {cont_9}')
print(f'Posição primeiro 3: {pos_3_final}')
print(f'Números pares: {tupla_numeros_pares}')

# --------------------------------------------------------

numeros = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))

print(f'Você digitou os valores{numeros}')
print(f'O número 9 apareceu {numeros.count(9)}')

if 3 in numeros:
    print(f'O número 3 apareceu na posição {numeros.index(3) + 1}')
else:
    print('O número 3 não foi digitado')

print('Números pares:', end=' ')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
