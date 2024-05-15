'''
mover 3 discos em três pinos
'''
def torre6(mov_disc, d1, d2, d3, pino1, pino2, pino3):
    if mov_disc == 1:
            print('Movendo o disco 1 para o pino 3')
            pino1[0][0] = 0
            print(pino1[0][0])
            print(pino1[1][0])
            print(pino1[2][0])
            print('#######')
            pino3[2][0] = 1
            print(pino3[0][0])
            print(pino3[1][0])
            print(pino3[2][0])
            print('#######')

    if mov_disc == 2:
        print('Movendo o disco 2 para o pino 2')
        pino1[1][0] = 0
        print(pino1[0][0])
        print(pino1[1][0])
        print(pino1[2][0])
        pino2[2][0] = 2
        print('#######')
        print(pino2[0][0])
        print(pino2[1][0])
        print(pino2[2][0])
        print('#######')
                 
    if mov_disc == 3:
        print('Movendo o disco 1 para o pino 2')
        pino3[2][0] = 0
        print(pino3[0][0])
        print(pino3[1][0])
        print(pino3[2][0])
        print('#######')
        pino2[1][0] = 1
        print(pino2[0][0])
        print(pino2[1][0])
        print(pino2[2][0])
        print('#######')

    if mov_disc == 4:
        print('Movendo o disco 3 para o pino 3')
        pino1[2][0] = 0
        print(pino1[0][0])
        print(pino1[1][0])
        print(pino1[2][0])
        print('#######')
        pino3[2][0] = 3
        print(pino3[0][0])
        print(pino3[1][0])
        print(pino3[2][0])
        print('#######')

    if mov_disc == 5:
        print('Movendo o disco 1 no pino 1')
        pino2[1][0] = 0
        print(pino2[0][0])
        print(pino2[1][0])
        print(pino2[2][0])
        print('#######')
        pino1[2][0] = 1
        print(pino1[0][0])
        print(pino1[1][0])
        print(pino1[2][0])
        print('#######')

    if mov_disc == 6:
        print('Movendo o disco 2 no pino 3')
        pino2[2][0] = 0
        print(pino2[0][0])
        print(pino2[1][0])
        print(pino2[2][0])
        print('#######')
        pino3[1][0] = 2
        print(pino3[0][0])
        print(pino3[1][0])
        print(pino3[2][0])
        print('#######')

def torre(mov_disc, d1, d2, d3, pino1, pino2, pino3):
    if mov_disc == 7:
        print('Movendo o disco 1 no pino 3')
        pino1[2][0] = 0
        print(pino1[0][0])
        print(pino1[1][0])
        print(pino1[2][0])
        print('#######')
        pino3[0][0] = 1
        return pino3

    else:  
        torre6(mov_disc + 1, d1, d2, d3, pino1, pino2, pino3)


#####################
mov_disc = 1
d1 = [1]
d2 = [2]
d3 = [3]
pino1 = [d1, d2, d3]
pino2 = [[0], [0], [0]]
pino3 = [[0], [0], [0]]
print('Pino 1: ')
print(pino1[0])
print(pino1[1])
print(pino1[2])
print('Pino 2: ')
print(pino2[0])
print(pino2[1])
print(pino2[2])
print('Pino 3: ')
print(pino3[0])
print(pino3[1])
print(pino3[2])
print('#######')
pino3 = torre(mov_disc, d1, d2, d3, pino1, pino2, pino3)
print(pino3)
