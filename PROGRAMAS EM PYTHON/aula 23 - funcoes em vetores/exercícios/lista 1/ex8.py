'''
8. Faça um Programa que peça a idade e a altura de 5
pessoas, armazene cada informação no seu
respectivo vetor. Imprima a idade e a altura na
ordem inversa a ordem lida
'''
def atribuicao_idade_altura(idade, altura):
    i = 0
    while (i <= 4):
        idadeP = int(input(f'Digite a idade da {i + 1}° pessoa: '))
        idade.append(idadeP)
        alturaP = float(input(f'Digite a altura da {i + 1}° pessoa: '))
        altura.append(alturaP)        
        i += 1
####################
idade = []
altura = [] 
idadeP = 0
alturaP = 0
atribuicao_idade_altura(idade, altura)
idade.reverse()
altura.reverse()
print(idade)
print(altura)
