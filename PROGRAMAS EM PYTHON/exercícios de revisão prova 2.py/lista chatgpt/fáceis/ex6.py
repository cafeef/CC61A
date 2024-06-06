'''
Implemente uma função recursiva para calcular o produto de dois números inteiros sem usar o operador de multiplicação.
'''
#Funções
def Calculo_Multiplicacao(n1, n2):
    if n2 == 1:
        return n1
    else:
        return n1 + Calculo_Multiplicacao(n1, n2 - 1)


#Programa principal
n1 = int(input('Digite 1° número que deseja calcular a multiplicação: '))
n2 = int(input('Digite o 2° número que deseja calcular a multiplicacão: '))
multiplicacao = Calculo_Multiplicacao(n1, n2)
print(f'A multiplicaçào entre {n1} e {n2} é {multiplicacao}')