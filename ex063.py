# ex063
# receba um número inteiro e mostre os elementos de uma sequencia fibonacci

quantidade = int(input('Digite um número: '))

fibonacci = [0, 1]
print(fibonacci)

while quantidade != 0:
    print(fibonacci[0], end='--> ')
    fibonacci[0] = fibonacci[0] + fibonacci[1]

    quantidade -= 1

print('Fim!!!')
