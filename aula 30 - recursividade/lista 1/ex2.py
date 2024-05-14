def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
####################
n = int(input('Digite o termo que deseja saber a sequência de fibonacci: '))
n -=1
fibonacci = fibonacci(n)
print(f'O {n + 1}° na sequência de fibonacci é: {fibonacci}')