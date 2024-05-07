'''
Crie um programa que leia uma matriz 5 x 5.
Leia também um valor X. O programa deverá
fazer a busca desse valor na matriz e, ao final,
escrever a localização (linha e coluna) ou uma
mensagem de “não encontrado”.
'''
def criacaoMatriz():
    matriz = []
    linha = 0
    while linha < 5:
        lista = []
        coluna = 0
        while coluna < 5:
            lista.append(randint(1, 5))
            coluna += 1
        matriz.append(lista)
        linha += 1
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print(matriz[3])
    print(matriz[4])
    return matriz

def localizacaoNumero(matriz, n):
    linha = 0
    localizacao = [0] * 2
    while (linha < 5):
        coluna = 0
        while (coluna < 5):
            if (matriz[linha][coluna] == n):
                localizacao[0] = linha + 1
                localizacao[1] = coluna + 1
                print(localizacao)
            coluna += 1
        linha += 1

#################
from random import randint
matriz = criacaoMatriz()
n = int(input('Digite o valor que deseja encontrar: '))
print('A(s) localização(ões) do número é(são): ')
localizacaoNumero(matriz, n)