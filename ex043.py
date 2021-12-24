# ex043
# Calule o IMC
# receba peso e altura e mostre o resultado conforme abaixo

# abaixo de 18.5 -> Abaixo do peso
# entre 18.5 e 25 -> Peso ideal
# entre 25 e 30 -> sobrepeso
# entre 30 e 40 -> Obesidade
# acima de 40 -> Obesidae mórbida

# IMC = Peso ÷ (Altura × Altura)
# IMC = 80 kg ÷ (1,80 m × 1,80 m) = 24,69 kg/m2 (Peso ideal)

peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros: '))

imc = (peso / (altura * altura))

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidae mórbida')


print('{:.2f}'.format(imc))
