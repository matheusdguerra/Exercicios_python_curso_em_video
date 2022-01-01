# ex077
# Criar uma tupla com várias palavras
# Mostrar quais são as vogais


tupla = ('Pao', 'Leite', 'Cafe', 'Arroz', 'Feijao', 'Massa', 'Tomate')
vogais = ('A', 'E', 'I', 'O', 'U')


for p in tupla:
    vagais_palavra = ('')
    print(f'Na palavra {p} temos:', end='')
    for v in p:
        if v.upper() in vogais:
            vagais_palavra = vagais_palavra + ' ' + v

    print(vagais_palavra)
