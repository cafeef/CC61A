def atribuicao_salario(salarios):
    venda = -1
    while (venda != 0):
        venda = int(input('Digite o valor bruto da venda realizada essa semana [0 para sair]: '))
        if (venda != 0):
            salario = calculo_salario(venda)
            salarios.append(salario)

def calculo_salario (venda):
    fixo = 200
    comissao = venda * 0.09
    salario = fixo + comissao
    return salario

def ordena_salarios(salarios):
    cont200 = 0
    cont300 = 0
    cont400 = 0
    cont500 = 0
    cont600 = 0
    cont700 = 0
    cont800 = 0
    cont900 = 0
    cont1000 = 0
    i = 0
    fim = len(salarios)
    while (fim >= 0):
        while (i <= (fim - 1)):
            if (salarios[i] >= 200 and salarios[i] < 299):
                cont200 += 1
            elif (salarios[i] >= 300 and salarios[i] < 399):
                cont300 += 1
            elif (salarios[i] >= 400 and salarios[i] < 499):
                cont400 += 1
            elif (salarios[i] >= 500 and salarios[i] < 599):
                cont500 += 1
            elif (salarios[i] >= 600 and salarios[i] < 699):
                cont600 += 1
            elif (salarios[i] >= 700 and salarios[i] < 799):
                cont700 += 1
            elif (salarios[i] >= 800 and salarios[i] < 899):
                cont800 += 1
            elif (salarios[i] >= 900 and salarios[i] < 999):
                cont900 += 1
            else:
                cont1000 += 1
            i += 1
        fim -= 1
    print(f'Nos salários digitados, há {cont200} vendedores com o salário entre R$200 e R$299.')
    print(f'Nos salários digitados, há {cont300} vendedores com o salário entre R$300 e R$399.')
    print(f'Nos salários digitados, há {cont400} vendedores com o salário entre R$400 e R$499.')
    print(f'Nos salários digitados, há {cont500} vendedores com o salário entre R$500 e R$599.')
    print(f'Nos salários digitados, há {cont600} vendedores com o salário entre R$600 e R$699.')
    print(f'Nos salários digitados, há {cont700} vendedores com o salário entre R$700 e R$799.')
    print(f'Nos salários digitados, há {cont800} vendedores com o salário entre R$800 e R$899.')
    print(f'Nos salários digitados, há {cont900} vendedores com o salário entre R$900 e R$999.')
    print(f'Nos salários digitados, há {cont1000} vendedores com o salário maior que R$1000.')
##############################
salarios = []
atribuicao_salario(salarios)
print(salarios)
ordena_salarios(salarios)