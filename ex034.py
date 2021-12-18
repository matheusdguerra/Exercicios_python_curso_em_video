# ex043
# receba um salário e mostre um aumento
# salarios superiores a 1250,00 aumente 10 %
# salarios inferioes ou iguais a 1250,00 aumente 15%

salario = float(input('Digite um salário: '))

if salario <= 1250.00:
    aumento = str('15%')
    novo_salario = salario + (salario * 0.15)
else:
    novo_salario = salario + (salario * 0.10)
    aumento = str('10%')
print('Novo salário aumentado em {} é de: {:.2f} R$'. format(aumento, novo_salario))
