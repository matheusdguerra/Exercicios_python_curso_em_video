# ex104
# crie uma função que valide apenas se a entrada for numerica

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido\33[m')
        if ok:
            break

    return(valor)


n = leiaint('Digite um numero: ')
print(f'Você digitou o numero {n}')
