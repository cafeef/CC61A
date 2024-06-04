'''
Desenvolva uma função recursiva para calcular a potência de um número, com base e expoente dados.
'''
#Funções
def CalculoPotencia(n, p):
    if p == 1:
        return n
    else:
        return n * CalculoPotencia(n, p - 1) 


#Programa principal
n = int(input('Digite o número que deseja calcular a potência: '))
p = int(input('Digite a potência desejada: '))
resultado = CalculoPotencia(n, p)
print(f'O resultado da potência é: {resultado}')