'''
Crie um programa que leia uma matriz 4 x 4
com números aleatórios (de 1 até 50), imprima
a matriz e retorne a localização (linha e a
coluna) do maior valor.
'''
def criacaoMatriz ():
    matriz = []
    linha = 0
    nM = 0
    localizacao = [0] * 2
    while (linha < 4):
        coluna = 0
        lista = []
        while (coluna < 4):
            lista.append(randint(1, 50))
            if lista[coluna] > nM:
                nM = lista[coluna]
                localizacao[0] = linha
                localizacao[1] = coluna
            coluna += 1
        matriz.append(lista)
        linha += 1

    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print(matriz[3])
    print('A localização do maior valor é:')
    print(localizacao)

##################
from random import randint
criacaoMatriz()