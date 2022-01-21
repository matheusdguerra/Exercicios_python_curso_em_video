# ex113
# crie uma função que valide numero interiro e outra que valide numero float
# crie tratamento de exeções

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))

        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar\33[m')
            return 0

        except:
            print('\033[0;31mERRO! Digite um número real válido\33[m')
            continue

        else:
            return(n)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))

        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar\33[m')
            return 0

        except:
            print('\033[0;31mERRO! Digite um número inteiro válido\33[m')
            continue

        else:
            return(n)


i = leiaint('Digite um inteiro: ')
f = leiafloat('Digite um real: ')
print(f'Você digitou o numero inteiro {i} e real {f}')
