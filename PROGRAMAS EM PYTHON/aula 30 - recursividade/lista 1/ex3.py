def somaTermos(n):
    tamanho = len(str(n))
    if tamanho == 1:
        return n
    else:
        divisao = n//10**(tamanho-1)
        resto = n%(10**(tamanho-1))
        return divisao + somaTermos(resto) 
#######################
n = int(input('Digite o número que deseja somar os termos: '))
soma = somaTermos(n)
print(f'A soma dos dígitos de {n} é: {soma}')

