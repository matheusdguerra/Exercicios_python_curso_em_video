def leiaint(msg):
    while True:
        try:
            n = int(input(msg))

        except KeyboardInterrupt:
            print('\033[0;31mUsuário preferiu não digitar\33[m')
            return 3

        except:
            print('\033[0;31mERRO! Digite um número inteiro válido\33[m')
            continue

        else:
            return(n)


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont += 1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc
