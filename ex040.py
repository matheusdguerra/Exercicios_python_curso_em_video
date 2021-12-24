# ex040
# Receba duas medias e mostre a nota final
# resultadao abaixo de 5 mostre reprovado
# media entre 5 e 6.9 mostre recuperação
# media superior a 7 mostre aprovado

mediaA = float(input('Digite a media A: '))
mediaB = float(input('Digite a media B: '))

media = ((mediaA + mediaB) / 2)

if media < 5.0:
    print('{} -> REPROVADO'.format(media))
elif 7 > media >= 5.0:
    print('{} -> RECUPERAÇÃO'.format(media))
else:
    print('{} -> APROVADO'.format(media))
