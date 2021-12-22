# ex038
# Receba 2 numero e informe se o primeiro ou o segundo é maior ou se ambos são iguais

primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))

if primeiro > segundo:
    print('O primeiro valor é o maior')
elif segundo > primeiro:
    print('O segundo valor é o maior')
else:
    print('Os valores são iguais')
