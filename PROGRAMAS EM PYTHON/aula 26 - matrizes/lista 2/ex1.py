'''
. Faça um programa que preenche uma matriz 4
x 4 com o produto do valor do índice da linha e
da coluna de cada elemento. Em seguida,
imprima na tela a matriz
'''

def criacaoMatriz():
    matriz = []
    linha = 0
    while (linha < 4):
        coluna = 0
        lista = []
        while (coluna < 4):
            lista.append(coluna * linha)
            coluna += 1
        matriz.append(lista)
        linha += 1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print(matriz[3])

############
criacaoMatriz()