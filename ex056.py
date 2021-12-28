# ex056
# receba nome, idade e sexo de 4 pessoas
# mostre:
# 1 -> Media de idade do grupo
# 2 -> Homem mais velho
# 3 -> Quantas mulheres tem menos de 20 anos

nomes = []
idades = []
sexos = []

for c in range(0, 4):
    nome = str(input('Digite o {}º nome: '.format(c + 1)))
    nomes.append(nome)

    idade = int(input('Digite a {}º idade: '.format(c + 1)))
    idades.append(idade)

    sexo = str(input('Digite o {}º sexo: '.format(c + 1)))
    sexos.append(sexo)

#####     Media das idades de todos     #####
idade_total = 0
for c in idades:
    idade_total += c

media = idade_total / 4
print('A média das idades é {}'.format(media))

#####     Homem mais velho     #####
nomes_homens_velhos = []
idades_homens_velhos = []

for n, i, s in zip(nomes, idades, sexos):
    if s in 'Mm':
        nomes_homens_velhos.append(n)
        idades_homens_velhos.append(i)

nome_homem_velho = nomes_homens_velhos[0]
idade_homem_velho = idades_homens_velhos[0]

for n, i in zip(nomes_homens_velhos, idades_homens_velhos):
    if i > idade_homem_velho:
        nome_homem_velho = n
        idade_homem_velho = i

print('O homem mais velho é: {} com {} anos.'.format(nome_homem_velho, idade_homem_velho))

#####     Quantidade de mulheres menores de 20 anos     #####

nomes_mulheres_menores = []

for n, i, s in zip(nomes, idades, sexos):
    if s in 'Ff' and i < 20:
        nomes_mulheres_menores.append(n)

print('As mulheres menores de 20 anos são {}'.format(nomes_mulheres_menores))

print(nomes)
print(idades)
print(sexos)
