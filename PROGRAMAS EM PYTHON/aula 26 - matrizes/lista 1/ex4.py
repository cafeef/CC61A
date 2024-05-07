'''
Faça um programa que leia uma matriz 3x3 de
inteiros e multiplique os elementos da
diagonal principal da matriz por um número
informado pelo usuário. Imprima a matriz na
tela antes e depois da multiplicação
'''

def lerMatriz():
    matriz = []
    lista = [] 
    linha = 0
    while (linha < 3):
        coluna = 0
        lista = []
        while (coluna < 3):
            lista.append(randint(0,5))
            coluna += 1
        matriz.append(lista)
        linha += 1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print('########')
    return matriz

def multiplicacaoMatriz(matriz, n):
    linha = 0
    while (linha < 3):
        coluna = 0
        while (coluna < 3):
            if linha == coluna:
                matriz[linha][coluna] = matriz[linha][coluna] * n
            coluna += 1
        linha += 1
    print(matriz [0])
    print(matriz[1])
    print(matriz[2])
################
from random import randint
matriz = lerMatriz()
n = int(input('Digite o número a ser multiplicado pela diagonal principal: '))
multiplicacaoMatriz(matriz, n)
