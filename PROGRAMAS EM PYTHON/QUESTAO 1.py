'''
triangular = seus divisores sao tres numeros consecutivos
'''
def verificaNumeroTriangular (n):
    cont = 1
    contd = 0
    while (cont <= n and contd < 3):
        if (n%cont == 0):
            if ((cont * (cont + 1) * (cont + 2)) == n):
                contd = contd + 2
        cont = cont + 1
        
        
    if (contd == 2):
        print('Esse número é triangular')
    else:
        print('Esse número não é triangular')

##################
cont = 1
while (cont <= 10):
    n = int(input('Digite um número inteiro: '))
    verificaNumeroTriangular(n)
    cont = cont + 1