# ex062
# receba o primeiro termo e a razão de uma progressão aritmetica
# mostre os 10 primeiros termos da progressão
# após mostrar os 10 pergunte se deseja mostrar mais itens da progressão

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

decimo = 0

while decimo != 10:
    print(primeiro_termo, end='--> ')
    primeiro_termo += razao
    decimo += 1

escolha = 1
quantidade = 1

while escolha != 0:
    escolha = int(input('\nDeseja visualizar mais quantos itens da progressão? '))
    quantidade = escolha
    while quantidade != 0:
        print(primeiro_termo, end='--> ')
        primeiro_termo += razao
        quantidade -= 1


print('FIM!!!')
