'''
7. Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da forma:
A[i][j] = 2*i + 7*j + 2   se i < j;
A[i][j] = 3*i^2 + 1   se i = j;
A[i][j] = 4*i^3 + 5*j^2 + 1   se i > j.
'''
def criacaoMatriz():
    matriz = []
    linha = 0
    indiceMatriz = 0
    while (linha < 10):
        coluna = 0
        lista = []
        while (coluna < 10):
            if (linha < coluna):
                elemento = 0
                elemento = (2*linha) + (7*coluna+ 2) 
                lista.append(elemento)
            elif(linha == coluna):
                elemento = 0
                elemento = (3*(linha**2)+ 1) 
                lista.append(elemento)
            elif (linha > coluna): 
                elemento = 0
                elemento = (4*(linha**3)) + (5*(coluna**2)+ 1)
                lista.append(elemento) 
            coluna += 1
        matriz.append(lista)
        linha += 1
    while(indiceMatriz < 10):
        print(matriz[indiceMatriz])
        indiceMatriz += 1
###################
criacaoMatriz()