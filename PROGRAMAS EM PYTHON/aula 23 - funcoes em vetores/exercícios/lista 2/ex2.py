def atribuicao_notas(notas):
    nota = 0
    while (nota != -1):
        nota = int(input('Digite a nota [-1 para sair]: '))
        if (nota != -1):
            notas.append(nota)

def quantidade_notas(notas):
    quantidadenotas = len(notas)
    print(f'A quantidade de notas digitadas foi: {quantidadenotas}')
    return quantidadenotas

def exibicao_notas(notas):
    print(f'As notas digitadas foram:')
    print(notas)
    print(f'Em ordem inversa: ')
    notas.reverse()
    print(notas)

def soma_media_notas(notas, mediaNotas):
    i = 0
    somaNotas = 0
    div = quantidadenotas
    while (div >= 0):
        while (i <= (div - 1)):
            somaNotas = somaNotas + notas[i]
            i += 1
        div -= 1
    print(f'A soma das notas foi: {somaNotas}')
    mediaNotas = somaNotas / quantidadenotas
    print(f'A média das notas foi: {mediaNotas}')
    return mediaNotas

def calculo_acima_media(notas, mediaNotas):
    i = 0
    fim = quantidadenotas
    cont_media = 0
    cont_nota7 = 0
    while (fim > 0):
        while (i <= (fim - 1)):
            if (notas[i] > mediaNotas):
                cont_media += 1
            if (notas[i] < 7):
                cont_nota7 += 1
            i += 1
        fim -= 1
    print(f'Há {cont_media} pessoas com nota acima da média.')
    print(f'Há {cont_nota7} pessoas com nota abaixo de 7.')

#################
notas = []
mediaNotas = 0
atribuicao_notas(notas)
quantidadenotas = quantidade_notas(notas)
exibicao_notas(notas)
mediaNotas = soma_media_notas(notas, mediaNotas)
calculo_acima_media(notas, mediaNotas)
print('Programa encerrado.')