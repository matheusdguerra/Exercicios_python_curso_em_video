nome = str(input('Nome: '))

if nome == 'Matheus':
    print('Nome bonito')
elif nome in ('Joao Maria'):
    print('Nome popular')
else:
    print('Nome comum')

print('Tenha um bom dia {}'.format(nome))
