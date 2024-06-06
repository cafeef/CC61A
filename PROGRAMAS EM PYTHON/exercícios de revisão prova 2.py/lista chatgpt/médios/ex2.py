'''
Implemente uma função recursiva para verificar se uma palavra é um palíndromo.
'''
#Funções
def Verificacao(palavra, tamanho, palavra_reverse):
    tamanho_reverse = len(palavra_reverse)
    if tamanho_reverse == tamanho:
        return palavra_reverse
    else:
        palavra_reverse = palavra_reverse + palavra[-1:]
        palavra = palavra[:-1]
        return Verificacao(palavra, tamanho, palavra_reverse)


#Programa Principal
palavra = input('Digite a palara que deseja verificar: ')
tamanho = len(palavra)
palavra_reverse = ''
tamanho_reverse = len(palavra_reverse)
print(palavra)
palavra_reverse = Verificacao(palavra, tamanho, palavra_reverse)
print(palavra_reverse)
if palavra_reverse == palavra:
    print('A palavra é palíndromo.')
else:
    print('A palavra não é um palíndromo.')