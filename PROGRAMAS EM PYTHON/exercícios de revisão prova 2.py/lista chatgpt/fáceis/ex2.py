'''
Implemente uma função recursiva para calcular a soma dos primeiros nnn números naturais.
'''
#Funções
def SomaNaturais(n):
    if n == 1:
        return 1
    else:
        return n + SomaNaturais(n - 1)

#Programa principal
n = int(input('Digite até que número deseja realizar a soma: '))
soma = SomaNaturais(n)
print(f'A soma dos naturais até {n} é {soma}')