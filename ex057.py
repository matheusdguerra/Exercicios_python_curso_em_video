# ex057
# Leia o sexo de uma pesso apenas no formato 'M' ou 'F'.
# Caso esteja errado peça par digitar novamente

flag = 0
while flag == 0:
    sexo = str(input('Digite o sexo da pessoa M/F: '))
    if sexo in 'MmFf':
        flag = 1
    else:
        flag = 0
