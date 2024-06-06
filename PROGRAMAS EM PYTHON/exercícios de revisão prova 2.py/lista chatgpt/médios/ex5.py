'''
Desenvolva uma função recursiva para calcular a sequência de Collatz para um número dado.
ni+1 = 3ni + 1 se ni for ímpar
ni+1 = ni/2 se ni for par.
. Faça um programa collatz.py que dado um número inteiro positivo, 
determina o número de repetições do procedimento para chegar em 1.
'''
#Funções
def Collatz(n, passos):
    if n == 1:
        return passos
    else:
        if n%2 == 0:
            return Collatz(n/2, passos + 1)
        else:
            return Collatz((3*n + 1), passos + 1)


#Programa principal
n = int(input('Digite o termo que deseja calcular os passos: '))
passos = 0
passos = Collatz(n, passos)
print(f'O número de passos foi: {passos}')