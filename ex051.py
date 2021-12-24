# ex051
# receba o primeiro termo e a razão de uma progressão aritmetica
#  mostre os 10 primeiros termos da progressão

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

if razao == 1:
    final = (10 * razao) + 1
else:
    final = 10 * razao

for c in range(primeiro_termo, final, razao):
    print(c)
