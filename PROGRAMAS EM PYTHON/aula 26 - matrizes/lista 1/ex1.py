matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
lista = []
linha = 0
contM = 0
while (linha < 3):
    coluna = 0
    while (coluna < 3):
        matriz[linha][coluna] = int(input(f'Qual o valor da {linha + 1}° linha e {coluna + 1}° coluna? '))
        if matriz[linha][coluna] > 5:
            contM += 1
        coluna += 1
    linha += 1

print(matriz[0])
print(matriz[1])
print(matriz[2])
print(f'A matriz elaborada possui {contM} números maiores que 5')