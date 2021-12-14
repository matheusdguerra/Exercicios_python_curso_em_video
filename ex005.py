''' 
Operadores aritméticos
+ Adição              -> 5+2 -> 7
- Subtração           -> 5-2 -> 3
* Multiplicação       -> 5*2 -> 10
/ Divisão             -> 5/2 -> 2.5
// Divisão inteira    -> 5//2 -> 2
** Potencia 5²        -> 5**2 -> 25 
% Resto da divisão    -> 5%2 -> 1

pow(5,2) Potencia porem perde ordem de procedencias
Raiz quadrada 25**(1/2)
Raiz cubica 127**(1/3)

Repetições

Ordem de procedência
1 ()
2 **
3 * / // %
4 + -
'''

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {} \nA multiplicação é {} \nA divisão é {:.2f} \nA divisao por inteiro é {} \nA potência é {}'.format(s, m, d, di, e))

# REPETIÇõES

nome = input('Qual o seu nome: ')
print('Prazer em conhecer {:20}'.format(nome), end='|-|')
print('Prazer em conhecer {:>20}'.format(nome), end='|-|')
print('Prazer em conhecer {:<20}'.format(nome), end='|-|')
print('Prazer em conhecer {:^20}'.format(nome), end='|-|')
print('Prazer em conhecer {:=^20}'.format(nome))

# Ex005
# Receba um número é mostre o sucessor e o antecessor

numero = int(input('Digite um número: '))

sucessor = numero + 1
antecessor = numero - 1

print('O antecessor de {} é {} \nO sucessor de {} é {}'.format(numero, antecessor, numero, sucessor))

print('O antecessor de {} é {} e o sucessor é {}'.format(numero, numero - 1, numero + 1))
