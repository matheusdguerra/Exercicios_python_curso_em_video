# ex042
# receba 3 comprimentos e diga se é pssivel fazer um triangulo

# mostre qual tipo de triangulo é formado
# Equilátero -> todos os lados são iguais
# Isósceles -> dois lados são iguais
# Escaleno -> todos os lados são diferentes

from random import sample

ldA = int(input('Digite o lado A: '))
ldB = int(input('Digite o lado B: '))
ldC = int(input('Digite o lado C: '))

if ldA > ldB and ldA > ldC:
    maior_numero = ldA
    sobras = ldB, ldC
elif ldB > ldC:
    maior_numero = ldB
    sobras = ldA, ldC
else:
    maior_numero = ldC
    sobras = ldA, ldB


if maior_numero < (sobras[0] + sobras[1]):
    print('É possível fazer um triângulo')

    if ldA == ldB == ldC:
        print('Triangulo Equilátero')
    elif ldA in (ldB, ldC) or ldB in (ldA, ldC):
        print('Triangulo Isósceles')
    else:
        print('Triangulo Escaleno')

else:
    print('Não é possível fazer um triângulo')


print(maior_numero)
print(sobras)
