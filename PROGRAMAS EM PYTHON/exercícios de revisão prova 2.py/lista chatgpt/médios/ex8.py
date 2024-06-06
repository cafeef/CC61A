'''
Problema: Soma dos Subconjuntos com Soma Máxima
Descrição:

Dado um conjunto de inteiros e um valor inteiro alvo S, encontre o subconjunto do conjunto dado cuja soma seja a maior possível sem exceder
S. Você deve usar recursividade para resolver este problema.
'''
#Funções
def SomaMaxima (lista, S, somaM, i, subconjunto):
    if i == len(lista) - 1:
        return subconjunto
    else:
        soma = lista[i] + lista[i + 1]
        if soma <= S:
            if somaM < soma:
                somaM = soma
                subconjunto = [lista[i], lista[i + 1]]
        return SomaMaxima(lista, S, somaM, i + 1, subconjunto)


#Programa principal
lista = []
i = 0
somaM = 0
subconjunto = []
while True:
    elemento = int(input('Digite o elemento da lista [0 para sair]: '))
    lista.append(elemento)
    if elemento == 0:
        break
S = int(input('Digite o alvo S: '))
subconjunto = SomaMaxima(lista, S, somaM, i, subconjunto)
somaM = subconjunto[0] + subconjunto[1]
print(subconjunto)
print(somaM)