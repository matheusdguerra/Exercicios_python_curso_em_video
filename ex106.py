# ex106
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.


# def escreva(p):
#    from time import sleep
#    t = len(p) + 24
#    print('\033[1;46m~\033[m' * t)
#    print(f'\033[1;46m  ACESSANDO MANUAL DO {p}  \033[m')
#    print('\033[1;46m~\033[m' * t)
#    sleep(2)
#
#
# def mostra_help(cmd):
#    from time import sleep
#    escreva(cmd)
#    print(f'\033[7;40m{help(cmd)}\033[m', flush=True)
#    sleep(2)
#
# Cor	        Fonte	    Fundo
# Preto	        \033[1;30m	\033[1;40m
# Vermelho      \033[1;31m	\033[1;41m
# Verde	        \033[1;32m	\033[1;42m
# Amarelo	    \033[1;33m	\033[1;43m
# Azul	        \033[1;34m	\033[1;44m
# Magenta	    \033[1;35m	\033[1;45m
# Cyan	        \033[1;36m	\033[1;46m
# Cinza Claro	\033[1;37m	\033[1;47
#
#
# while True:
#    print('\033[1;42m~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
#    print('\033[1;42m  SISTEMA DE AJUDA PYHELP  \033[m')
#    print('\033[1;42m~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
#
#    comando = str(input('Digite o comando: ')).lower()
#
#    if comando == 'fim':
#        print('\033[1;41m~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
#        print('\033[1;41m  SAINDO DO SISTEMA PYHELP  \033[m')
#        print('\033[1;41m~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m')
#        break
#    else:
#        mostra_help(comando)
#
# ----------------------------------------------------------------------------

c = ('\033[m',          # 0 -> Sem cor
     '\033[0;30;41m',   # 1 -> Vermelho
     '\033[0;30;42m',   # 2 -> Verde
     '\033[0;30;43m',   # 3 -> Amarelo
     '\033[0;30;44m',   # 4 -> Azul
     '\033[0;30;45m',   # 5 -> Roxo
     '\033[7;40m'       # 6 -> Branco
     )


def titulo(msg, cor=0):
    from time import sleep
    t = len(msg) + 4
    print(c[cor])
    print('~' * t)
    print(f'  {msg}  ')
    print('~' * t)
    print(c[0])
    sleep(1)


def ajuda(cmd):
    from time import sleep
    titulo(f'Acessando o manual do comando {cmd}', 4)
    print(c[6])
    help(cmd)
    print(c[0])
    sleep(1)


while True:

    titulo('SISTEMA DE AJUDA PYHELP', 2)

    comando = str(input('Digite o comando: ')).lower()

    if comando == 'fim':
        titulo('SAINDO DO SISTEMA PYHELP', 1)

        break
    else:
        ajuda(comando)

titulo('Até Logo!', 3)
