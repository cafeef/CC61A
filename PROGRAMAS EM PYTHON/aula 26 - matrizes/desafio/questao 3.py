'''
3. Escreva uma função para verificar se duas matrizes são iguais.
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

def verificacaoMatriz(matriz1, matriz2):
    linha = 0
    resposta = 1
    coluna = 0
    if (matriz1[linha][coluna] == matriz2[linha][coluna]):
        resposta = 0
        while (linha < 3):
            coluna = 0
            while (coluna < 3):
                if (matriz1[linha][coluna] == matriz2[linha][coluna]):
                    resposta = 0
                else: 
                    resposta = 1
                coluna += 1
            linha += 1
    else: 
        resposta = 1
    return resposta

######################
from random import randint
matriz1 = criacaoMatriz()
matriz2 = criacaoMatriz()
retorno = verificacaoMatriz(matriz1, matriz2)
if retorno == 1:
    print('As matrizes não são iguais.')
elif retorno == 0:
    print('As matrizes são iguais.')