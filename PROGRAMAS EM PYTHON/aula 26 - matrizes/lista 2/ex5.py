'''
 Crie um programa que leia duas matrizes 4 x 4
e escreva, em uma terceira matriz, os maiores
valores de cada posição das matrizes lidas.
Exemplo
matrizA[0][0] = 10
matrizB[0][0] = 15
matrizC[0][0] = 15
'''

def criacaoMatriz1 ():
    matriz = []
    linha = 0
    while (linha < 4):
        coluna = 0
        lista = []
        while (coluna < 4):
            lista.append(randint(0, 5))
            coluna += 1
        matriz.append(lista)
        linha += 1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print(matriz[3])
    print('#########')
    return matriz

def criacao_matriz3 (matriz1, matriz2):
    matriz = []
    linha = 0
    while (linha < 4):
        coluna = 0
        lista = []
        while (coluna < 4):
            if matriz1[linha][coluna] > matriz2[linha][coluna]:
                lista.append(matriz1[linha][coluna])
            else:
                lista.append(matriz2[linha][coluna])
            coluna += 1
        matriz.append(lista)
        linha += 1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print(matriz[3])
####################
from random import randint
matriz1 = criacaoMatriz1()
matriz2 = criacaoMatriz1()
criacao_matriz3(matriz1, matriz2)