'''
Escreva uma função recursiva para calcular o número de maneiras de subir uma escada de nnn degraus, 
podendo subir 1, 2 ou 3 degraus por vez.
'''
#Funções
def CalculoDegraus(n, qtd_sub):
    if n%qtd_sub == 0:
        return n/qtd_sub
    else:
        return CalculoDegraus(n - 1, qtd_sub)
    


#Programa principal
n = int(input('Digite o número de degrais: '))
qtd = 0
qtd_sub = 1
qtd_total = 0
while qtd_sub <= 3:
    qtd = CalculoDegraus(n, qtd_sub)
    print(f'A quantidade para {qtd_sub} degraus é de: {qtd}')
    qtd_total += qtd
    qtd_sub += 1

print(f'A quantidade total de formas de subir a escada de {n} degraus é de: {qtd_total}')

