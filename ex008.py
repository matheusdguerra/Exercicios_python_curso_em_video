# ex008
# Receba um valor em metros e mostre convertido em centimetros e milimetros
# km hm dam m dm cm mm

valor = float(input('Digite um comprimento em metros: '))

km = valor * 0.001
hm = valor * 0.01
dam = valor * 0.1
dm = valor * 10
cm = valor * 100
mm = valor * 1000

print('O valor em km é? {}\nO valor em hm é: {}\nO valor em dam é {}\nO valor em dm é {}\nO valor em cm é: {}\nO valor em mm é: {}'.format(km, hm, dam, dm, cm, mm))
