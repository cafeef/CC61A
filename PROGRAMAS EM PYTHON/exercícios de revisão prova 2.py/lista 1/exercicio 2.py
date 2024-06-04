lista = []
fim = 10
i = 0
cont = 1
SomaElementos = 0
while (fim >= 0):
    while i <=  (fim - 1):
        lista.append(cont)
        lista[i] = lista[i]**2
        SomaElementos += lista[i]
        cont += 1
        i += 1
    fim -= 1

print(lista)
print(SomaElementos)