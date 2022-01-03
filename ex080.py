# ex080
# receba 5 valores e coloque em uma lista já me ordem crescente sem usar sort
# no final mostres a lista ordenada

lista = []

for cont in range(0, 5):
    numero = int(input(f'Digite o {cont + 1}º valor: '))
    if cont == 0:
        lista.append(numero)
    else:
        for idx, c in enumerate(lista):
            if numero < lista[0]:  # o '<=' irá adicionar números repetidos.
                lista.insert(0, numero)
                break
            elif numero > lista[-1]:  # o '>=' irá adicionar números repetidos.
                lista.append(numero)
                break
            # elif numero >= c and numero <= lista[idx + 1]: # o '>= e <=' irá adicionar números repetidos.
            elif numero > c and numero < lista[idx + 1]:  # o '> e <' não irá adicionar números repetidos.
                # print(f'C{c}')
                # print(f'IDX+1{idx + 1}')
                # print(f'IDX{idx}')
                lista.insert(idx + 1, numero)
                break

    print(lista)

print(lista)
