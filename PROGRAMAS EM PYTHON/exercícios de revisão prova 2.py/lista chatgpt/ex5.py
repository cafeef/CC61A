'''
Escreva uma função recursiva para calcular o máximo divisor comum (MDC) de dois números.
'''
#Funções
def calculo_mdc(n1, n2, mdc):
    if n1%mdc == 0 and n2%mdc == 0:
        return mdc
    else: 
        return calculo_mdc(n1, n2, mdc - 1)


#Programa principal
n1 = int(input('Digite o primeiro número que deseja calcular o MDC: '))
n2 = int(input('Digite o segundo número que deseja calcular o MDC: '))
if n1 > n2:
    mdc = n2
if n2 > n1:
    mdc = n1
mdc = calculo_mdc(n1, n2, mdc)
print(f'O mdc entre {n1} e {n2} é {mdc}')