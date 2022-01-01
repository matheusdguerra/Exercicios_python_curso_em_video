# ex073
# monte uma tupla com 20 times
# mostre:
# 1 -> apenas os 5 primeiros
# 2 -> Os ultimos 4
# 3 -> A lista em ordem alfabeticas
# 4 -> Posção do chapecoense

organizador = '+-' * 60
cont = 0
times = (
    'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
    'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio',
    'Bahia', 'Sport', 'Chapecoense')

print(organizador)
print(f'5 Primeiros colocados {times[0:5]}')
print(organizador)
print(f'4 Últimos colocados {times[-4:]}')
print(organizador)
print(f'Ordem alfabética {sorted(times)}')
print(organizador)

print(f'Chapecoense {times.index("Chapecoense") + 1}ª')

for c in times:
    cont += 1
    if c == 'Chapecoense':
        print(f'Chapecoense {cont}ª')
print(organizador)
