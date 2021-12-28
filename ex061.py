# ex061
# receba o primeiro termo e a razão de uma progressão aritmetica
# mostre os 10 primeiros termos da progressão

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

decimo = 0

while decimo != 10:
    print(primeiro_termo, end='--> ')
    primeiro_termo += razao
    decimo += 1

print('FIM!!!')
