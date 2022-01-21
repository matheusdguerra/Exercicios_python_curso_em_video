# import uteis  # se o modulo uteis não existir da exeção ModuleNotFounfError
#
# primt('oi')  # > Erro sintatico
# print(x)  # erro semantico exeção NomeError
#
# n = int(input('Número: '))  # se digitar uma string da exeção ValueError
#
# a = int(input('Numerador: '))
# b = int(input('Denominador: '))  # Se digitar 0 da a exeção ZeroDivisionError
# c = a/b
#
# r = 2/'2'  # Exeção TypeError
# lst = [3, 6, 4]
# print(lst[3])  # não há indice 3 da exeção IndexError


# -> Exceção ................ Causa do erro
# -> AssertionError ......... Gerado quando uma assert instrução falha.
# -> AttributeError ......... Gerado quando a atribuição ou referência de atributo falha.
# -> EOFError ............... Gerado quando a input()função atinge a condição de fim de arquivo.
# -> FloatingPointError ..... Gerado quando uma operação de ponto flutuante falha.
# -> GeneratorExit .......... Aumenta quando o método de um gerador close() é chamado.
# -> ImportError ............ Gerado quando o módulo importado não é encontrado.
# -> IndexError ............. Gerado quando o índice de uma sequência está fora do intervalo.
# -> KeyError ............... Gerado quando uma chave não é encontrada em um dicionário.
# -> KeyboardInterrupt ...... Gerado quando o usuário pressiona a tecla de interrupção ( Ctrl+C ou Delete).
# -> MemoryError ............ Gerado quando uma operação fica sem memória.
# -> NameError .............. Gerado quando uma variável não é encontrada no escopo local ou global.
# -> NotImplementedError .... Gerado por métodos abstratos.
# -> OSError ................ Gerado quando a operação do sistema causa um erro relacionado ao sistema.
# -> OverflowError .......... Gerado quando o resultado de uma operação aritmética é muito grande para ser representado.
# -> ReferenceError ......... Gerado quando um proxy de referência fraco é usado para acessar um referente coletado de lixo.
# -> RuntimeError ........... Gerado quando um erro não se enquadra em nenhuma outra categoria.
# -> StopIteration .......... Gerado pela next() função para indicar que não há mais nenhum item a ser retornado pelo iterador.
# -> SyntaxError ............ Gerado pelo analisador quando um erro de sintaxe é encontrado.
# -> IndentationError ....... Gerado quando há recuo incorreto.
# -> TabError ............... Gerado quando o recuo consiste em tabulações e espaços inconsistentes.
# -> SystemError ............ Gerado quando o intérprete detecta um erro interno.
# -> SystemExit ............. Elevado por sys.exit() função.
# -> TypeError .............. Gerado quando uma função ou operação é aplicada a um objeto de tipo incorreto.
# -> UnboundLocalError ...... Gerado quando uma referência é feita a uma variável local em uma função ou método, mas nenhum valor foi vinculado a essa variável.
# -> UnicodeError ........... Gerado quando ocorre um erro de codificação ou decodificação relacionado ao Unicode.
# -> UnicodeEncodeError ..... Gerado quando ocorre um erro relacionado ao Unicode durante a codificação.
# -> UnicodeDecodeError	..... Gerado quando ocorre um erro relacionado ao Unicode durante a decodificação.
# -> UnicodeTranslateError .. Gerado quando ocorre um erro relacionado ao Unicode durante a tradução.
# -> ValueError ............. Gerado quando uma função obtém um argumento de tipo correto, mas valor impróprio.
# -> ZeroDivisionError ...... Gerado quando o segundo operando da divisão ou operação do módulo é zero.

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))  # Se digitar 0 da a exeção ZeroDivisionError
    c = a/b

except (ValueError, TypeError):
    print('Problema com os tipos de dados digitados')

except ZeroDivisionError:
    print('Não é possivel dividir por zero')

except KeyboardInterrupt:
    print('Usuário não informou dados')

except Exception as erro:  # Se der erro
    print(f'Erro! {erro.__cause__}')

else:  # Se não der erro
    print(f'{c:.2f}')

finally:    # Se der erro ou não der erro
    print('Volte Sempre')
