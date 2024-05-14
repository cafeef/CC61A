def mdc(n1, n2, cont):
    if (n1%cont == 0 and n2%cont == 0):
            return cont
    else:
        return mdc(n1, n2, cont - 1)
    

##################
n1 = int(input('Digite o primeiro número que deseja calcular o MDC: '))
n2 = int(input('Digite o segundo número que deseja calcular o MDC: '))
if (n1 > n2):
        cont = n2
else: 
        cont = n1
mdc = mdc(n1, n2, cont)
print(f'O mdc de {n1} e {n2} é: {mdc}')