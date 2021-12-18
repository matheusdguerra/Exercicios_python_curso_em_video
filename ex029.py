# ex029
# receba a velocidade de um carro
# se ele ultrapassar 80km mostre uma mensagem de multa
# O valor será 7,00 por km acima do limite

velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80:
    valor_multa = (velocidade - 80) * 7
    print('A sua velocidade {} está acima do permitido!\nVocê foi multado em {:.2f} R$'.format(velocidade, float(valor_multa)))
else:
    print('Sua velocidade {}km/h e igual ou abaixo de 80km/h'.format(velocidade))
