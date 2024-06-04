'''
Crie uma função recursiva para inverter uma lista.
'''
#Funções
def Inversao(lista, lista_invertida):
    tamanho = len(lista)
    if tamanho == 0:
        return lista_invertida
    else:
        lista_invertida.append(lista[-1:])
        del(lista[-1:])
        return Inversao(lista, lista_invertida)


#Programa principal
lista = []
lista_invertida = []
while True:
    n = int(input('Digite os números da lista que deseja inverter [0 para sair]: '))
    if n == 0:
        break
    lista.append(n)

lista_invertida = Inversao(lista, lista_invertida)
print(lista_invertida)
