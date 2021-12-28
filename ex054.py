# ex054
# leia uma data de nascimento de 7 pessoas
# liste as pessoas maiores e menores de 18 anos

from datetime import date

datas = []
datas_maiores_21 = []
datas_menores_21 = []

for c in range(0, 7):
    data = str(input('Digite a {}º data: '.format(c + 1)))
    datas.append(data)

ano_atual = date.today().year

for c in datas:
    if int(c[6:10]) < ano_atual - 21:
        datas_maiores_21.append(c)
    else:
        datas_menores_21.append(c)

print('Quantida de maiores de 21 ano: {}'.format(len(datas_maiores_21)))
print(datas_maiores_21)
print('+-' * 30)
print('Quantida de menores de 21 ano: {}'.format(len(datas_menores_21)))
print(datas_menores_21)
