'''
10. Faça um programa que receba a temperatura
média de cada mês do ano e armazene-as em uma
lista. Após isto, calcule a média anual das
temperaturas e mostre todas as temperaturas 
'''

def atribuicao_temp (temperaturas):
    i = 0
    fim = 12
    while (fim >= 0):
        while (i <= (fim - 1)):
            temperaturaP = float(input(f'Digite a {i + 1}° média mensal: '))
            temperaturas.append(temperaturaP)
            i += 1
        fim -= 1
    print(temperaturas)

def calculo_media_anual(temperaturas):
    i = 0
    fim = 12
    somaTemps = 0
    mediaAnual = 0
    while (fim >= 0):
        while (i <= (fim - 1)):
            somaTemps += temperaturas[i]
            i += 1
        fim -= 1
    print(f'A soma de todas as médias mensais foi: {somaTemps}')
    mediaAnual = somaTemps / 12
    print(f'A média anual das temperaturas foi de: {mediaAnual}')


#######################

temperaturas = []
atribuicao_temp(temperaturas)
calculo_media_anual(temperaturas)