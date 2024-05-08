'''
Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
'''
def criacaoMatriz():
    matriz = []
    linha = 0 
    while (linha < 4):
        coluna = 0
        lista = []
        while (coluna < 4):
            lista.append(randint(0,20))
            coluna += 1
        matriz.append(lista)
        linha += 1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print(matriz[3])
    return matriz

def verificaNumero(matriz):
    linha = 0
    cont10 = 0
    while (linha < 4):
        coluna = 0 
        while (coluna < 4):
            if (matriz[linha][coluna] > 10):
                cont10 += 1
            coluna += 1
        linha += 1 
    print(f'Na matriz elaborada, há {cont10} número(os) maior(oes) que 10.')

############
from random import randint
matriz = criacaoMatriz()
verificaNumero(matriz)