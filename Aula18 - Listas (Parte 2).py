# Variaveis compostas [LISTAS]
# Tupals são mutáveis

teste = list()

teste.append('Matheus')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['ana', 15], ['Pedro', 59], ['Rodrigo', 5]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[3][1])
print(galera[1][1])

for c in galera:
    print(f'{c[0]} tem {c[1]} anos de idade')

galera = []
dado = []
maior = menor = 0

for c in range(0, 3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('idade:')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Temos {maior} maiores de idade')
print(f'Temos {menor} menores de idade')
