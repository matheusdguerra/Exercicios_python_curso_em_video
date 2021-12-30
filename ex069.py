# ex069
# leia diversas idades e sexos
# perguntar se deseja ou não coninuar o cadastros de novas pessoas
# No final mostre:
# -> Quantas pessoas tem mais de 18 anos
# -> Quantos homens cadastrados
# -> Quantas mulheres com menos de 20 anos

mulher_maior = homens = pessoas_maiores = 0

while True:
    idade = int(input('Digite uma idade.....: '))
    sexo = str(input('Digite um sexo [M/F].: '))

    if sexo in ('FfMm'):
        if idade > 18:
            pessoas_maiores += 1
        if sexo in ('Mm'):
            homens += 1
        if sexo in ('Ff') and idade > 20:
            mulher_maior += 1
    else:
        print('Digite um sexo válido!')

    escolha = str(input('Deseja continuar [S/N]: '))
    if escolha in ('SsNn'):
        if escolha in ('Nn'):
            break

print(f'Pessoas maiores de 18 anos: {pessoas_maiores}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres maires de 20 anos: {mulher_maior}')
