# Receba nome e media de um aluno.
# conforme a media tambem guarde a situação
# > 7 aprovado
# < 7 reprovado

boletim = {}

boletim['nome_aluno'] = str(input('Digite o nome do aluno: '))
boletim['media'] = float(input(f'Digite a media de {boletim["nome_aluno"]}: '))

print(f'O nome é {boletim["nome_aluno"]}')
print(f'A média é {boletim["media"]}')

if boletim["media"] >= 7:
    boletim['situacao'] = 'Aprovado'
elif 5 <= boletim["media"] < 7:
    boletim['situacao'] = 'Recuperação'
else:
    boletim['situacao'] = 'Reprovado'

print(boletim)
print('=-' * 30)
for k, i in boletim.items():
    print(f'{k} = {i}')
