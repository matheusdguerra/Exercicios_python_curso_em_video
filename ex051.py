# ex051
# receba o primeiro termo e a razão de uma progressão aritmetica
# mostre os 10 primeiros termos da progressão

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

decimo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo + 1, razao):
    print(c, end='--> ')

print('FIM!!!')
