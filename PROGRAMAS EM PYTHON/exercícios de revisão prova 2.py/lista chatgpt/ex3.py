'''
Crie uma função recursiva para calcular a sequência de Fibonacci até o n-ésimo termo.
'''
#Funções
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


#Programa principal
n = int(input('Digite até que número deseja calcular a sequência de fibonacci: '))
n_fibonacci = fibonacci(n)
print(f'O número de fibonacci até o {n}° termo é: {n_fibonacci}')