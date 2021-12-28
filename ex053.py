# ex053
# leia uma frase e diga se é um palindromo
# APOS A SOPA

# frase = 'APOS A SOPA'
# frase = 'A SACADA DA CASA'
# frase = 'A TORRE DA DERROTA'
# frase = 'O LOBO AMA O BOLO'
frase = 'ANOTARAM A DATA DA MARATONA'

frase = frase.replace(' ', '')
print(frase)

frase_len = len(frase)
for c in frase:
    if c == frase[frase_len - 1]:
        resultado = 'É Palindromo!'
    else:
        for c in frase:
            print(frase[frase_len - 1], end='')
            frase_len -= 1
        resultado = '\nNão é Palindromo'
        break

    frase_len -= 1

print(resultado)
