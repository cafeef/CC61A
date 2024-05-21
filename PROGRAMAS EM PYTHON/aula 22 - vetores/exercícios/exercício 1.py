votacao = []
relatorio = [0] * 3
print('Bem vindo a cabine de votação. [0] para sair. ')
print('[1] CANDITADO 1')
print('[2] CANDITADO 2')
print('[3] CANDITADO 3')
voto = int(input('Digite em quer quer votar: '))
while (voto != 0):
        if voto == 1:
            votacao.append(voto) 
            relatorio[0] += 1
        if voto == 2: 
            votacao.append(voto)
            relatorio[1] += 1
        if voto == 3:
            votacao.append(voto)
            relatorio[2] += 1 
        voto = int(input('Digite em quer quer votar [0] para sair.: '))        
print('Aqui está o resultado da eleição: ')
print(f'CANDITADO 1: {relatorio[0]} votos.')
print(f'CANDITADO 2: {relatorio[1]} votos.')
print(f'CANDITADO 3: {relatorio[2]} votos.')
maiorV = max(relatorio)
i = 0
fim = len(relatorio)
while (fim >= 0):
    while(i <= (fim -1)):
        if relatorio[i] == maiorV:
            CanGanha = i + 1
        i += 1
    fim -= 1

print(f'O canditado ganhador foi: CANDITADO {CanGanha} e fez {maiorV} votos.')