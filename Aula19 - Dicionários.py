# Variaveis compostas [Dicionários]

pessoas = {'nome': 'Matheus', 'sexo': 'M', 'idade': 32}
print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']

for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['nome'] = 'Pedro'

for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['peso'] = 62

for k, v in pessoas.items():
    print(f'{k} = {v}')

# ------------------------------------------------------------------------------

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])

print(brasil[0]['uf'])
print(brasil[1]['sigla'])


estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
