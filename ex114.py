# ex114
# testar se um site está no ar.
# tratando as exeções


import urllib
import urllib.request

site = str(input('Insira o site: '))
try:
    site1 = urllib.request.urlopen('http://www.'+site+'/')
except urllib.request.URLError:
    print('O Site não está acessível no momento')
else:
    print('Consegui abrir o site com sucesso!')
    print(site1.read())
