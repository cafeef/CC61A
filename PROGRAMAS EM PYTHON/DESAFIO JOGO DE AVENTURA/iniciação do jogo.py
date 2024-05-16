def inicio():
    print('------------------\n SEJA BEM VINDO!  \nESCOLHA UMA OPÇÃO:\n------------------ ')
    print('[1] INICIAR O JOGO \n[2] SAIR')
    r = int(input(''))
    return r

#############

r = inicio()
while r != 1 or r != 2:
    r = inicio()