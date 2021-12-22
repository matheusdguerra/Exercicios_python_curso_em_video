# ex037
# Receba um número inteiro
# receba uma base de conversão
# 1 -> binário
# 2 -> octal
# 3 -> hexadecimal
# mostre o numero convertido

numero = int(input('Dgite um número inteiro: '))
base_conversao = int(input('Digite a base de conversão: '))

if base_conversao == 1:
    numero = bin(numero)[2:]
    print('Binário {}'.format(numero))
elif base_conversao == 2:
    numero = oct(numero)[2:]
    print('Octal {}'.format(numero))
elif base_conversao == 3:
    numero = hex(numero)[2:]
    print('Hexadecimal {}'.format(numero))
else:
    print('Base de conversão incorreta')
