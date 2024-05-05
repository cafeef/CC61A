'''
7. Faça um Programa que leia um vetor de 5 números
inteiros, mostre a soma, a multiplicação e os
números.
'''
from random import randint
vetor = [0] * 5
i = 0
soma = 0
multiplicacao = 1
while (i <= 4):
    vetor[i] = randint(1, 10)
    soma += vetor[i]
    multiplicacao = multiplicacao * vetor[i]
    i += 1
print(soma)
print(multiplicacao)
print(vetor)