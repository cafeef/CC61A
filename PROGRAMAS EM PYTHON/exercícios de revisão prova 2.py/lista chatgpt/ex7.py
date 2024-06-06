'''
Crie uma função recursiva para encontrar o n-ésimo termo da sequência de Tribonacci.
'''
#Funções
def tribonacci(n):
    if n == 2:
        return 1
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
#Programa principal
n = int(input('Digite o n-ésimo termo que deseja encontrar: '))
termo = tribonacci(n)
print(f'O {n}° termo da sequência de tribonacci é {termo}')