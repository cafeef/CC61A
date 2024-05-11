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

def multiplicacaoMatriz(matriz):
    for linha in range(3):
        for coluna in range(3):
            matriz[linha][coluna] *= 5
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
####################
from random import randint
matriz = criacaoMatriz()
multiplicacaoMatriz(matriz)