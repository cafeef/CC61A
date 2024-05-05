'''
9. Foram anotadas as idades e alturas de 10 alunos.
Faça um Programa que determine quantos alunos
com mais de 13 anos possuem altura inferior à
média de altura desses alunos.
'''
def atribuicao_idade_altura(idade, altura):
    i = 0
    fim = 10
    while(fim >= 0):
        while (i <= (fim - 1)):
            idadeP = int(input(f'Digite a idade do {i + 1}° aluno: '))
            idade.append(idadeP)
            alturaP = float(input(f'Digite a altura do {i + 1}° aluno: '))
            altura.append(alturaP)
            i += 1
        fim -= 1

def calculo_somaemedia_altura(altura, somaAlturas, mediaAlturas):
    i = 0
    fim = 10
    while (fim >= 0):
        while (i <= (fim - 1)):
            somaAlturas = somaAlturas + altura[i]
            i += 1
        fim -= 1
    print(f'A soma das alturas foi: {somaAlturas}')
    mediaAlturas = somaAlturas / 10
    print(f'A média das alturas foi: {mediaAlturas}')

def contagem_alunos(altura, idade, mediaAlturas):
    i = 0
    fim = 10
    contAlunos = 0
    while (fim >= 0):
        while (i <= (fim - 1)):
            if (idade[i] > 13):
                if (altura[i] < mediaAlturas):
                    contAlunos = contAlunos + 1
            i += 1
        fim -= 1
    print(f'Na lista informada, há {contAlunos} maiores de 13 anos que possui a altura menor que a média.')

##############
idade = []
altura = []
somaAlturas = 0
mediaAlturas = 0
atribuicao_idade_altura(idade, altura)
calculo_somaemedia_altura(altura, somaAlturas, mediaAlturas)
contagem_alunos(altura, idade, mediaAlturas)
