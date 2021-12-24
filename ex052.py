# ex052
# receba um número e diga se ele é primo

numero = int(input('Digite um numero: '))
status_primo = 'É Primo'

for c in range(1, numero + 1):
    # print(c)
    if c not in [1, numero]:
        if numero % c == 0:
            # print('IF', c)
            status_primo = 'Não é Primo'

print(status_primo)
