'''
2. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
elementos. Escreva ao final a matriz obtida.
'''
def criacaoMatriz(tamanho):
    matriz = []
    linha = 0
    indiceMatriz = 0
    while (linha < tamanho):
        coluna = 0
        lista = []
        while (coluna < tamanho):
            if (linha == coluna):
                lista.append(1)
            else: 
                lista.append(0)
            coluna += 1
        matriz.append(lista)
        linha += 1
    while (indiceMatriz < tamanho):
        print(matriz[indiceMatriz])
        indiceMatriz += 1
##############
tamanho = int(input('Digite o tamanho da matriz identidade que deseja: '))
criacaoMatriz(tamanho)