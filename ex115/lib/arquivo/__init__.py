from ex115.lib.interface import cabecalho


def arquivoexiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()

    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro para criar o arquivos')
    else:
        print(f'Arquivo {nome} criado pois nao existia!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'a')
        # a -> append mode
        # r -> Readlines
        # w -> Overwrites
    except:
        print('Houve erro para abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro em tempo de excrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
