'''
Escreva uma função recursiva para calcular o fatorial de um número.
'''
#Funções
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


#Programa principal
n = int(input('Digite o número que deseja calcular o fatorial: '))
f = fatorial(n)
print(f'O fatorial de {n} é {f}')