'''
Escreva a função que recebe 2 argumentos: o
primeiro argumento é um vetor de inteiros e o
segundo argumento é um número. A função deve
retornar quantas vezes o número ocorre dentro do
vetor.
'''
from random import randint
def retorno_numeros(vetor, n):
    fim = len(vetor)
    i = 0
    cont_rep = 0
    while (fim > 0):
        while(i <= (fim - 1)):
            if (vetor[i] == n):
                cont_rep += 1
            i += 1
        fim -= 1
    print(f'O número de repeticoes do elemento selecionado na lista é de: {cont_rep}')
###############################
vetor = []
vetor = list(range(randint(1, 11)))
n = randint(1, 10)
print(n)
print(vetor)
retorno_numeros(vetor, n)