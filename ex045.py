# ex045
# faça o computador jogar jokenpô

from random import choice
from time import sleep

escolha_usuario = str(input('Digte pedra, tesoura ou papel: '))

escolhas_computador = ["pedra", "tesoura", "papel"]

escolha_computador = (choice(escolhas_computador))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-' * 10)

if escolha_usuario == escolha_computador:
    print('Empate')
elif escolha_computador == 'pedra' and escolha_usuario == 'tesoura':
    print('Computador Ganhou')
elif escolha_computador == 'pedra' and escolha_usuario == 'papel':
    print('Usuário Ganhou')
elif escolha_computador == 'tesoura' and escolha_usuario == 'pedra':
    print('Usuário Ganhou')
elif escolha_computador == 'tesoura' and escolha_usuario == 'papel':
    print('Computador Ganhou')
elif escolha_computador == 'papel' and escolha_usuario == 'tesoura':
    print('Computador Ganhou')
elif escolha_computador == 'papel' and escolha_usuario == 'pedra':
    print('Usuário Ganhou')

print(escolha_computador, escolha_usuario)
print('=-' * 10)
