# ex059
# leia 2 valores e apresente um menu
# 1 -> Somar
# 2 -> multiplicar
# 3 -> maior
# 4 -> novos numeros
# 5 -> sair do programa

flag = 0

while flag != 5:
    valorA = float(input('Digite valor A: '))
    valorB = float(input('Digite valor B: '))
    op = int(input('\n1 -> Somar\n2 -> Multiplicar\n3 -> maior\n4 -> novos numeros\n5 -> sair\n\nDigite uma operação: '))
    if op == 1:
        print('A soma é {}'.format(valorA + valorB))
    elif op == 2:
        print('A multiplicação é {}'.format(valorA * valorB))
    elif op == 3:
        if valorA > valorB:
            print('O mairo valor é {}'.format(valorA))
        else:
            print('O mairo valor é {}'.format(valorB))
    elif op == 4:
        pass
    elif op == 5:
        flag = 5
    else:
        print('Operação inválida')
