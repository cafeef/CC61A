'''
Implemente uma função recursiva para encontrar o n-ésimo termo da sequência de Tetranacci.
0, 1, 1, 2
'''
#Funções
def Tetranacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return Tetranacci(n - 1) + Tetranacci(n - 2) + Tetranacci(n - 3) + Tetranacci(n - 4)


#Programa principal
n = int(input('Digite o n-ésimo termo que deseja encontrar na sequencia de Tetranacci: '))
tretanacci = Tetranacci(n)
print(f'O {n}° termo é: {tretanacci}')