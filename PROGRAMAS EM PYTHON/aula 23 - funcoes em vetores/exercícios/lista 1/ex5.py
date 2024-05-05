'''
5. Armazenar 10 valores inteiros num vetor de 10
posições. Sequencialmente, imprima-os em ordem
inversa multiplicados por 2.
'''
def manipulacao_vetor(vetor, i):
    i = 0
    fim = len(vetor)
    while (fim > 0):
        while (i <= (fim - 1)):
            vetor[i] = vetor[i] * 2
            i += 1
        fim -= 1
#########################
from random import randint
vetor = [0] * 10
i = 0
while (i <= 9):
    vetor[i] = randint(1,10)
    i += 1

print(vetor)
manipulacao_vetor(vetor, i)
vetor.reverse()
print(vetor)