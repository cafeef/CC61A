'''
6. Faça um Programa que leia 20 números inteiros e
armazene-os num vetor. Armazene os números
pares no vetor PAR e os números IMPARES no
vetor impar. Imprima os três vetores.
'''
def atribuicao_vetor(vetor):
    i = 0
    while (i <= 19):
        vetor[i] = randint(1, 10)
        i += 1

def atribuicao_parouimpar (vetor):
    i = 0
    fim = len(vetor)
    while (fim > 0):
        while (i <= (fim - 1)):
            if (vetor[i]%2 == 0):
                par.append(vetor[i])
            else: 
                impar.append(vetor[i])
            i += 1
        fim -= 1
##########################3
from random import randint
vetor = [0] * 20
par = []
impar = []

atribuicao_vetor(vetor)
print(vetor)
atribuicao_parouimpar (vetor)
print('Lista par:')
print(par)
print('Lista ímpar:')
print(impar)