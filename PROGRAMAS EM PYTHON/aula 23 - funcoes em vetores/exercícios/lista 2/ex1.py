'''
1. Faça um programa que receba do usuário dez temperaturas em graus Fahrenheit, transformeas em graus Celsius e armazene os resultados em um vetor. Terminada a entrada de dados,
os valores armazenados devem ser apresentados. Obs.: A fórmula é C = 5/9 (F – 32).
'''
def atribuicao_temp (tempC):
    i = 0
    fim = 10
    while (fim >= 0):
        while (i <= (fim -1)):
            tempFah = int(input(f'Digite a {i + 1}° temperatura em F°: '))
            tempFah_conversao = 5/9*(tempFah - 32)
            tempC.append(round(tempFah_conversao, 2))
            i += 1
        fim -= 1
    print(tempC)
#################
tempC = []
atribuicao_temp(tempC)