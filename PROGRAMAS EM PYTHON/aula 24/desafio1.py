def atribuicao_salario (salario):
    n = 1    
    while (n != 0):
        n = int(input('Digite o salário a ser calculado [0 para sair]: '))
        listaDeSalarios.append(n)
    print('Atribuicao encerrada.')

def abonoSalarial(listaDeSalarios):
    bonusSalario = []
    i = 0
    while (listaDeSalarios[i] != 0):
        if ((listaDeSalarios[i])* 0.20) < 100:
            bonusSalario.append(100)
        else:
            bonusSalario.append(0.20 * listaDeSalarios[i])
        i+= 1
    return bonusSalario

#####################
listaDeSalarios = []
atribuicao_salario(listaDeSalarios)
print(listaDeSalarios)

i = 0
bonusSalario = abonoSalarial(listaDeSalarios)
fim = len(bonusSalario)
contF = 0
mB = 0
while (fim >= 0):
    while (i <= (fim - 1)):
        if (bonusSalario[i] == 100):
            contF += 1
        if (bonusSalario[i] > mB):
            mB = bonusSalario[i]
        i += 1
    fim -= 1
print(f'A quantidade de funcionário que receberam o abono é de: {contF}')
print(f'O maior abono foi de: {mB}')


