# ex083
# receba uma expressão matemárica
# VÁLIDA -> ((a + B) * c)
# INVÁLIDA -> ((a + b) * c -> falta um parentese
# INVÁLIDA -> 6 + ) 85 ( -> ordem incorreta

expressao = list(input('Digite uma expressão matemática: '))
lista_teste = []
'''
quantidade_a = expressao.count('(')
quantidade_b = expressao.count(')')

if quantidade_a == quantidade_b:
    print('Expressão válida')
else:
    print('Expressão inválida')

print(expressao)
'''

for c in expressao:
    if c == '(':
        lista_teste.append(c)
    elif c == ')':
        if len(lista_teste) > 0:
            lista_teste.pop()
        else:
            lista_teste.append(c)

if len(lista_teste) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')
