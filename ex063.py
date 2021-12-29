# ex063
# receba um número inteiro e mostre os elementos de uma sequencia fibonacci

quantidade = int(input('Digite um número: '))

lista_fibonacci = [0, 1]

while quantidade != 2:

    fibonacci = lista_fibonacci[-1] + lista_fibonacci[-2]
    lista_fibonacci.append(fibonacci)
    quantidade -= 1

print(lista_fibonacci)
print('Fim!!!')
