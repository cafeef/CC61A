'''
4. Faça um programa que lê um vetor de 3 elementos e uma matriz de 3 x 3 elementos. 
Em seguida o programa deve fazer a multiplicação do vetor pelas colunas da matriz.  
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

def criacaoVetor():
    vetor = []
    i = 0
    fim = 3
    while (fim >= 0):
        while(i <= (fim - 1)):
            vetor.append(randint(0,5))
            i += 1
        fim -= 1
    print(vetor)
    print('############')
    return vetor

def multiplicacaoMatriz(matriz, vetor):
    linha = 0
    matrizM = []
    while (linha < 3):
        coluna = 0
        i = 0
        lista = []
        while (coluna < 3):
            elemento = matriz[linha][coluna] * vetor[i]
            lista.append(elemento)
            coluna += 1
            i += 1
        matrizM.append(lista)
        linha += 1
    print(matrizM[0])
    print(matrizM[1])
    print(matrizM[2])

###################

from random import randint
matriz = criacaoMatriz()
vetor = criacaoVetor()
multiplicacaoMatriz(matriz, vetor)