# ex069
# leia diversas idades e sexos
# perguntar se deseja ou não coninuar o cadastros de novas pessoas
# No final mostre:
# -> Quantas pessoas tem mais de 18 anos
# -> Quantos homens cadastrados
# -> Quantas mulheres com menos de 20 anos

mulher_menor = homens = pessoas_maiores = 0

while True:
    idade = int(input('Digite uma idade.....: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite um sexo [M/F].: ')).strip().upper()[0]

    if idade >= 18:
        pessoas_maiores += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulher_menor += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Pessoas maiores de 18 anos: {pessoas_maiores}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres menores de 20 anos: {mulher_menor}')
