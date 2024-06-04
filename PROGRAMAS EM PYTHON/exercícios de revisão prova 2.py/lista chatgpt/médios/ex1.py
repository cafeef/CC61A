'''
Desenvolva uma função recursiva para calcular a soma dos dígitos de um número inteiro.
'''
#Funções
def SomaDigitos(n):
    tamanho = len(str(n))
    if tamanho == 1:
        return n
    else:
        digito = n // (10** (tamanho - 1))
        resto = n% (10 ** (tamanho - 1))
        return digito + SomaDigitos(resto)


#Programa principal
n = int(input('Digite o número que deseja somar os dígitos: '))
soma = SomaDigitos(n)
print(f'A soma dos dígitos é {soma}')
