# Módulos
# Organização do codigo / Divisão do código
# Facilita manutenção
# Ocultação do código detalhado
# Reutilização do código em outros projetos

import Aula22_uteis

num = int(input('Digite um valor: '))
fat = Aula22_uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O triplo de {num} é {Aula22_uteis.dobro(num)}')
print(f'O triplo de {num} é {Aula22_uteis.triplo(num)}')

# Pacotes
# Junção de modulos/funções separado por assuntos
# A separação é feita por pastas cada conjuntos de moduls fia dentro de um arquivos chamado __ini__.py
