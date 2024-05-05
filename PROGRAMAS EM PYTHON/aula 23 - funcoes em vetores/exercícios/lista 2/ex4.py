def atribuicao_votos(votos):
    voto = -1 
    while (voto != 0):
        voto = int(input('Digite o número da camisa do jogador: '))
        if (voto != 0 and voto >= 1 and voto <= 23):
            votos.append(voto)
            print('Voto computado.')
        if (voto < 1 or voto > 23):
            print('Número inválido, digite novamente.')
    print('Votação encerrada.')

def exibicao_resultados(votos):
    i = 0
    quant_votos = 23
    print(f'A quantidade de votos realizado é: {quant_votos}')
    fim = quant_votos
    mV = 0
    mJ = 0
    while (fim >= 0):
        while (i <= (fim - 1)):
            quantidade = votos.count(i + 1)
            print(f'O jogador {i + 1} recebeu {quantidade} votos.')
            porcentagem = round((quantidade / quant_votos) * 100, 1)
            print(f'O jogador {i + 1} obteve {porcentagem}% dos votos.')
            if (quantidade > mV):
                mV = quantidade
                mJ = votos[i]
                pM = round((mV / quant_votos) * 100, 1)
            i += 1
        fim -= 1
    print(f'O melhor jogador foi o {mJ}, pois teve {mV} votos e {pM}%.')

#####################
votos = []
from collections import Counter
atribuicao_votos(votos)
exibicao_resultados(votos)