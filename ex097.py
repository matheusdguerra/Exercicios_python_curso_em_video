# ex097
# crie uma função escreva() que escreva uma palavra qualquer entre duas linhas com o smesmo tamanho da palavra
# ex:
# ~~~~~~~~~
# OLÁ MUNDO
# ~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~
# PROGRAMAÇÃO COM PYTHON
# ~~~~~~~~~~~~~~~~~~~~~~

def escreva(p):
    t = len(p) + 4
    print('~' * t)
    print(f'  {p}  ')
    # {:^20}
    print('~' * t)


palavra = str(input('Digite uma palavra: '))
escreva(palavra)
