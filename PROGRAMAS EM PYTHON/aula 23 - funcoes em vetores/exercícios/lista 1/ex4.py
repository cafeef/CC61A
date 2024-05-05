'''
4. Faça um programa que leia dois vetores A e B
contendo, cada um, 10 elementos inteiros.
Intercale estes dois conjuntos (A[1] - B[1] - A[2] -
B[2]) formando um novo vetor de 20 elementos.
Imprima o novo vetor.
'''
from random import randint
v1 = [0] * 10
v2 = [0] * 10
v3 = []
i = 0
while (i <= 9):
    v1[i] = randint(1,10)
    v2[i] = randint(1,10)
    v3.append(v1[i])
    v3.append(v2[i])
    i += 1
print(v1)
print(v2)
print(v3)