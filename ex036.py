# ex036
# Aprovação de emprestimo
# Receba valor da casa, salario e anos para pagar
# Calcule valor da prestação mensal. Não excedenndo 30% do salario ou então será negado

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
anos = int(input('Digite a quantidade de anos para pagar: '))

prestacao_mensal = valor_casa / (anos * 12)
porcentagem_salario = salario * 0.30

if prestacao_mensal > porcentagem_salario:
    print('\33[31mEmprestimo negado.\33[m')
    print('Valor da prestação: {:.2f}\n30% do salário: {:.2f}'.format(prestacao_mensal, porcentagem_salario))
else:
    print('\33[32mEmprestimo aprovado\33[m')
    print('Valor da prestação: {:.2f}\n30% do salário: {:.2f}'.format(prestacao_mensal, porcentagem_salario))
