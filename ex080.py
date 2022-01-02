# ex080
# receba 5 valores e coloque em uma lista já me ordem crescente sem usar sort
# no final mostres a lista ordenada
'''
lista = []

for cont in range(0, 3):
    numero = int(input(f'Digite o {cont + 1}º valor: '))
    if cont == 0:
        lista.append(numero)
    elif cont == 1:
        if numero > lista[0]:
            lista.insert(1, numero)
        else:
            lista.insert(0, numero)
    elif cont == 2:
        if numero > lista[0] and numero < lista[1]:
            lista.insert(1, numero)
        elif numero < lista[0]:
            lista.insert(0, numero)
        else:
            lista.insert(2, numero)

    print(lista)

print(lista)
'''
# --------------------------------------------------------------------------

lista = []

for cont in range(0, 3):
    numero = int(input(f'Digite o {cont + 1}º valor: '))
    if cont == 0:
        lista.append(numero)
    else:
        while lista:
            if numero < lista[cont - 1]:
                lista.insert(cont - 1, numero)
                break
            elif numero > lista[cont - 1]:
                lista.insert(cont, numero)
                break

    print(lista)

print(lista)
