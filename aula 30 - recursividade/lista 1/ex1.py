def fatorial(n):
    if n == 1:
        return 1
    else: 
        return n * fatorial(n - 1)
###################
n = int(input('Digite o número que deseja calcular o fatorial: '))
fatorial = fatorial(n)
print(f'O fatorial do termo {n} é: {fatorial}')