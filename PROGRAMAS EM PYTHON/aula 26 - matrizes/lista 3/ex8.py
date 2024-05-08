'''
. Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão acima
da diagonal principal.
'''
def criacaoMatriz():
    matriz = []
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
    return matriz

def calculoSoma(matriz):
    soma = 0
    linha = 0
    while (linha < 3):
        coluna = 0
        while (coluna < 3):
            if (linha < coluna):
                soma = soma + matriz[linha][coluna]
            coluna += 1
        linha += 1
    print(f'A soma dos números acima da diagonal principal é: {soma}')
        
################
from random import randint
matriz = criacaoMatriz()
calculoSoma(matriz)