lista = [1, 2, 3, 4, 5, 6, 7, 8]
tamanho = len(lista)
i = 0
indicemet1 = tamanho - 1
metade = tamanho//2
met1 = []
met2 = []
listaNova = [met1, met2]
if tamanho%2 == 0:
    while metade > 0:
        met1.append(lista[indicemet1])
        met2.append(lista[i])
        indicemet1 -= 1
        i += 1
        metade -= 1
if tamanho%2 > 0:
    metade += 1
    while metade > 0:
        met1.append(lista[indicemet1])
        met2.append(lista[i])
        indicemet1 -= 1
        i += 1
        metade -= 1
    met2.remove(i)
print(lista)
print(met1)
print(met2)
print(listaNova)

        