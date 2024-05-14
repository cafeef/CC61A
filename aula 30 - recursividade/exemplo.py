def SomaLista(numeros):
    if len(numeros) == 1:
        return numeros[0]
    else:
        return numeros[0] + SomaLista(numeros[1:])
        
    
numeros = [1, 3, 5, 7, 9]
print(SomaLista(numeros))