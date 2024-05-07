'''
Faça um programa que leia uma matriz 3x3 de
inteiros e retorne a linha de maior soma.
Imprima na tela a matriz, a linha de maior
soma e a soma
'''

def criacaoMatrizes(): 
    matriz = []
    linha = 0
    while (linha < 3):
        lista = []
        coluna = 0
        while (coluna < 3):
            lista.append(randint(0, 5))
            coluna += 1
        matriz.append(lista)
        linha += 1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print('#########')
    return matriz

def somaMatriz(matriz):
    somaM = 0
    linha = 0
    while (linha < 3):
        soma = 0
        coluna = 0
        lista = []
        while (coluna < 3):
            soma = soma + matriz[linha][coluna]
            coluna += 1
        if (soma > somaM):
            somaM = soma
            lista.append(matriz[linha])
        linha += 1
    print(f'A linha de maior soma é a: ')
    print(lista)
    print(f'A maior soma é: {somaM}')

####################
from random import randint
matriz = criacaoMatrizes()
somaMatriz(matriz)