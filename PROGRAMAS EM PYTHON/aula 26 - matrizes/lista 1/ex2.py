def LeMatriz():
    matriz = []
    linha = 0 
    while (linha < 4):
        lista = []
        coluna = 0 
        while (coluna < 4):
            lista.append(randint(0,5))
            coluna += 1
        matriz.append(lista)
        linha += 1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print(matriz[3])
    return matriz

def somaMatriz (matriz):
    soma = 0
    linha = 0 
    while (linha < 4):
        coluna = 0
        while (coluna < 4):
            soma = soma + matriz[linha][coluna]
            coluna += 1
        linha += 1
    print(f'A soma dos elementos da matriz é {soma}')
#################
from random import randint
matriz = LeMatriz()
somaMatriz(matriz)