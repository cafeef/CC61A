'''
2. Dado um vetor com 10 elementos inteiros,
substituir cada elemento por ele mesmo
multiplicado pela posição do elemento no vetor
'''
def subst_elementos(vetor):
    fim = len(vetor)
    i = 0
    while (fim >= 0):
        while (i <= (fim - 1)):
            vetor[i] = vetor[i] * i
            i += 1
        fim -= 1
################
vetor = []
vetor = list(range(1, 11))
print(vetor)
print('Após a multiplicacao de cada elemento: ')
subst_elementos(vetor)
print(vetor)

