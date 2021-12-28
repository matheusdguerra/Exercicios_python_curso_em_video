# ex052
# receba um número e diga se ele é primo

numero = int(input('Digite um numero: '))
status_primo = 'É Primo'

for c in range(1, numero + 1):
    if numero == 1:
        status_primo = 'Não é Primo'
        break

    # print(c)
    if c not in [1, numero]:
        if numero % c == 0:
            #print('IF', c)
            status_primo = 'Não é Primo'


print(status_primo)

#### ------------------------------------------------------------------ ###
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')

    print('{}'.format(c), end='')

print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, tot))

if tot == 2:
    print('E por isso ele é Primo')
else:
    print('E por isso ele não é Primo')
