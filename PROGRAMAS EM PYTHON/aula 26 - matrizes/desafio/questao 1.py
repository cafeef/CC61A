'''
Escreva uma função para somar duas matrizes. As matrizes devem ter as mesmas dimensões.
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

def somaMatriz(matriz1, matriz2):
    linha = 0
    matriz = []
    while (linha < 3):
        lista = []
        coluna = 0
        while coluna < 3:
            soma = 0
            soma = matriz1[linha][coluna] + matriz2[linha][coluna]
            lista.append(soma)
            coluna += 1
        matriz.append(lista)
        linha += 1
    return matriz

#######################
from random import randint
matriz1 = criacaoMatriz()
matriz2 = criacaoMatriz()
matriz3 = somaMatriz(matriz1, matriz2)
print('A soma das duas matrizes é: ')
print(matriz3[0])
print(matriz3[1])
print(matriz3[2])