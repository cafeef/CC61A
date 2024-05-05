'''
1. Armazenar 10 valores inteiros num vetor de 10
posições. Após, leia o vetor e mostre os valores
armazenados, adicionando em 10 unidades
quando forem números pares
'''
def somapar(vetor):
    i = 0
    fim = len(vetor)
    while (fim >= 0):
        while (i <= (fim - 1)):
            if (vetor[i]%2 == 0):
                vetor[i] = vetor[i] + 10
            i += 1
        fim -= 1
####################
vetor = []
vetor = list(range(1, 11))
print(vetor)
print('Ao somar 10 unidades em valores pares: ')
somapar(vetor)
print(vetor)
