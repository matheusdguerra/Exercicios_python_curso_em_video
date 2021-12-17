# ex026
# Receba uma frase e mostre quantas vezes aparece a letra 'A' e qual posição a letra 'A' aparece pela primeira e ultima vez.

frase = str(input('Digite uma fraze: ')).lower().strip()

print('A frase possui {} letras A'.format(frase.count("a")))
print('Primeira aparição: {}'.format(frase.find("a")+1))
print('Ultima aparição: {}'.format(frase.rfind("a")+1))
