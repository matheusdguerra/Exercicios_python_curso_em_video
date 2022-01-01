# ex072
# monte um tupla de 0 a 20 por extenso
# receba um numero e mostre o se nome por extenso

numero_por_extenso = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
    'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', ' Vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break

print(f'Número por extenso: {numero_por_extenso[numero]}')
