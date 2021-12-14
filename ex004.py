
# Testes tipos primitivos

algo = input('Digite algo: ')

print('O tipo primitivo desse valor é?', type(algo))
print('Só tem espaço?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabetico?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em maiusculas?', algo.isupper())
print('Está em minusculas?', algo.islower())
print('Está capitalizada?', algo.istitle())
