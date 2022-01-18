# criei um modulo que tenha as funções aumentar(), dominuir() dobro() metade()
# faça um programa que importe e use esses modulos

from ex107_utilidadesCeV import moeda
from ex107_utilidadesCeV import dado

p = dado.leiadinheiro('Digite um preço: R$')
moeda.resumo(p, 10, 22)
