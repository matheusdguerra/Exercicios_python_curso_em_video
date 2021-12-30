# ex067
# receba vários numeros e mostre a tabuada
# interrompa quando for digitado um valor negativo

while True:
    numero = int(input('Digite um numero (negativo para sair): '))
    if numero < 0:
        break
    for c in range(0, 11):
        print(f'{c} x {numero} = {c * numero}')
