# ex024
# receba no nome de uma cidade e diga se ela começa com "santo"

cidade = input('Digite o nome de uma cidade: ')

cidade = cidade.split()

print('Inicia com Santo? {}'.format('santo' in cidade[0].lower()))
