
'''
\033[0;33;44m

# Estilo

0 normal
1 negrito
4 sublinhado
7 inverte

# Cores
Cor	        Fonte	    Fundo
Preto	    \033[1;30m	\033[1;40m
Vermelho    \033[1;31m	\033[1;41m
Verde	    \033[1;32m	\033[1;42m
Amarelo	    \033[1;33m	\033[1;43m
Azul	    \033[1;34m	\033[1;44m
Magenta	    \033[1;35m	\033[1;45m
Cyan	    \033[1;36m	\033[1;46m
Cinza Claro	\033[1;37m	\033[1;47m

\033[0; 30; 41m
\033[4; 33; 44m
\033[1; 35; 43m
\033[20; 42m
\033[m
\033[7:30m
'''

print('\033[7;33;44mOlá Mundo!\033[m')

a = 5
b = 3
print('Os números são \33[35m{}\33[m e \33[31m{}\33[m!!!'.format(a, b))

nome = 'Matheus'
print('Seja bem vindo {}{}{}!!!'.format('\33[32m', nome, '\33[m'))


nome = 'Matheus'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Seja bem vindo {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
