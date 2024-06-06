'''
Escreva uma função recursiva para encontrar a soma de todos os elementos em uma lista.
'''
#Função
def SomaLista(lista, soma):
    tamanho = len(lista)
    if tamanho == 0:
        return soma
    else:
        soma = soma + lista[0]
        del(lista[0])
        return SomaLista(lista, soma)


#Programa principal
soma = 0
lista = []
while True:
    n = int(input('Digite os números que deseja somar [0 para sair]: '))
    if n == 0:
        break
    lista.append(n)

soma = SomaLista(lista, soma)
print(f'A soma total dos elementos da lista é: {soma}')