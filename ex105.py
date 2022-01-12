# ex105
# crie uma função notas() que receba várias notas e retorna um dicionario com as seguintes informações
# ->OK  Quantidade de notas
# ->OK  A maior nota
# ->OK  A menor nota
# -> A media do turma
# -> A situação (opcional)

# Crie uma docstring


def notas(* num, sit=False):
    '''
    Função para analisar notas e situações de vários alunos
        :param n -> Uma ou mais notas dos alunos (aceita várias)
        :param sit -> valor opcional, indicando se deve ou não adicionar a situação
        :retun -> Dicionário com várias informações sobre a situação da turma
    '''
    boletin = {}
    cont = 0
    soma_notas = maior = menor = 0

    for c in num:
        if cont == 0:
            maior = menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c

        soma_notas += c
        cont += 1

    media = soma_notas / cont
    boletin['total'] = cont
    boletin['maior'] = maior
    boletin['menor'] = menor
    boletin['media'] = media

    if sit:
        if media < 6:
            situacao = 'REPROVADO'
        elif media > 6 and media < 7:
            situacao = 'RECUPERAÇÃO'
        else:
            situacao = 'APROVADO'

        boletin['situacao'] = situacao

    return(boletin)


help(notas)
resp = notas(7.0, 7.5, 7.0, sit=True)
print(resp)

# -------------------------------------------------------------------------------


def notas2(* num, sit=False):
    boletin = {}
    boletin['total'] = len(num)
    boletin['maior'] = max(num)
    boletin['menor'] = min(num)
    boletin['media'] = sum(num) / len(num)

    if sit:
        if boletin['media'] >= 7:
            situacao = 'BOA'
        elif boletin['media'] >= 5:
            situacao = 'RAZOAVEL'
        else:
            situacao = 'RUIM'

        boletin['situacao'] = situacao
    return(boletin)


resp = notas2(7.0, 7.5, 7.0, sit=True)
print(resp)
