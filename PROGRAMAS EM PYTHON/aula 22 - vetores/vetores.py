def bubble_sort(notas):
    fim = 10
    i = 0
    while (fim > 0):
        while (i < (fim - 1)):
            if (notas[i] < notas[i + 1]):
                temp = notas[i + 1]
                notas[i + 1] = notas[i]
                notas[i] = temp
            i += 1
        fim -= 1
###################
notas = [0] * 10
#alunos = [" "] * 10
n = 0
while (n < 10):
    #alunos[n] = input(f'Digite o nome do {n + 1}° aluno: ')
    notas[n] = int(input(f'Digite a {n + 1}° nota: '))
    n += 1
bubble_sort(notas)
print(notas)
#print(alunos)