# ex057
# Leia o sexo de uma pesso apenas no formato 'M' ou 'F'.
# Caso esteja errado peça par digitar novamente

flag = 0
while flag == 0:
    sexo = str(input('Digite o sexo da pessoa M/F: ')).strip().upper()[0]
    if sexo in 'MF':
        flag = 1
        print('Você digitou o sexo {} valido'.format(sexo))
    else:
        print('Sexo inválido, digite novamente.')
