'''
Crie um programa crie duas matrizes de
mesma dimensão (3x3) e, em uma terceira
matriz, armazene a soma das matrizes A e B
'''

def criacaoMatriz1():
    matriz = []
    linha = 0 
    while (linha < 3):
        coluna = 0
        lista = []
        while (coluna < 3):
            lista.append(randint(0, 5))
            coluna += 1
        matriz.append(lista)
        linha += 1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print('+')
    return matriz

def criacaoMatriz2():
    matriz = []
    linha = 0 
    while (linha < 3):
        coluna = 0
        lista = []
        while (coluna < 3):
            lista.append(randint(0, 5))
            coluna += 1
        matriz.append(lista)
        linha += 1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print('=')
    return matriz

def somaMatrizes(matriz1, matriz2):
    matriz = []
    linha = 0 
    while (linha < 3):
        coluna = 0
        lista = [] 
        while (coluna < 3):
            lista.append(matriz1[linha][coluna] + matriz2[linha][coluna])
            coluna += 1
        matriz.append(lista)
        linha += 1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    return matriz

#####################
from random import randint
matriz1 = criacaoMatriz1()
matriz2 = criacaoMatriz2()
matriz3 = somaMatrizes(matriz1, matriz2)