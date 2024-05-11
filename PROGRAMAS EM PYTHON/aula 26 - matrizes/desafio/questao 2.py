'''
Escreva uma função para transpor uma matriz (trocar linhas por colunas).
'''
def criacaoMatriz():
    matriz = []
    linha = 0
    while (linha < 3):
        coluna = 0
        lista = []
        while coluna < 3:
            lista.append(randint(0,5))
            coluna += 1
        matriz.append(lista)
        linha += 1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print('###########')
    return matriz


def matrizTransposta(matriz):
    matrizT = []
    linha = 0
    while (linha < 3):
        coluna = 0
        lista = []
        while (coluna < 3):
            lista.append(matriz[coluna][linha])
            coluna += 1
        matrizT.append(lista)
        linha += 1
    print(matrizT[0])
    print(matrizT[1])
    print(matrizT[2])



######################
from random import randint
matriz = criacaoMatriz()
matrizTransposta(matriz)