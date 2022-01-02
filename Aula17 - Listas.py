# Variaveis compostas [LISTAS]
# Tupals são mutáveis

# Criar lista vazia
# lista = []
# lista = list()

lista = ['A', 'B', 'C', 'D']
lista[3] = 'E'
print(lista)

# insere no final
lista.append('F')
print(lista)

# insere na posição 2 o 0
lista.insert(2, '0')
print(lista)

del lista[3]  # elimina pela posição
lista.pop(2)  # elimina pela posição
lista.pop()  # Elimina o último
lista.remove('A')  # elimina a primeira ocorrencia pelo coteúdo

# Remove se existe
if 'F' in lista:
    lista.remove('F')

valores = list(range(4, 11))
print(valores)

lista_valores = [6, 9, 3, 5, 1, 8, 2]
print(f'Lista inicial: {lista_valores}')
lista_valores.sort()
print(f'Lista Sort: {lista_valores}')
lista_valores.sort(reverse=True)
print(f'Lista Sort reversa: {lista_valores}')
print(f'Tamanho da lista: {len(lista_valores)}')


num = []
num.append(5)
num.append(9)
num.append(4)
for idx, v in enumerate(num):
    print(f'Achei na posição {idx} o valor {v}...')
print('Cheguei no final da lista')


valores_2 = list()
for cont in range(0, 5):
    valores_2.append(int(input('Digite um valor: ')))
for idx, c in enumerate(valores_2):
    print(f'{idx} {c}')

a = [6, 4, 6, 8]
b = a  # Ligação entre duas listas
print(a)
print(b)

b[2] = 0  # irá mudar o valor da lista a e b
print(a)
print(b)

b = a[:]  # copia de uma lista
b[2] = 1  # não irá alterar o valor da lista a
print(a)
print(b)
