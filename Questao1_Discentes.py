#Funções
def ExibicaoTurmas(turmas):
    turmas_exibir = turmas
    tamanho_exibir = len(turmas_exibir[0])
    i = 0
    while tamanho_exibir >= 0:
        while i <= tamanho_exibir - 1:
            print(f'- Turma {turmas_exibir[0][i]} com {turmas_exibir[1][i]} vagas')
            i += 1
        tamanho_exibir -= 1


def MatriculaTurmas(turmas, discentes, reserva):
    if len(discentes[0]) == 0:
        return reserva
    else:
        if discentes[1][0] == turmas[0][0]:
            if turmas[1][0] > 0:
                print(f'{discentes[0][0]} matriculado(a) com sucesso na turma {turmas[0][0]}.')
                turmas[1][0] -= 1
            else:
                print(f'Não há vagas na turma {turmas[0][0]}, encaminhando {discentes[0][0]} para a lista de espera...')
                reserva.append(discentes[0][0])
        if discentes[1][0] == turmas[0][1]:
            if turmas[1][1] > 0:
                print(f'{discentes[0][0]} matriculado(a) com sucesso na turma {turmas[0][1]}.')
                turmas[1][1] -= 1
            else:
                print(f'Não há vagas na turma {turmas[0][1]}, encaminhando {discentes[0][0]} para a lista de espera...')
                reserva.append(discentes[0][0])
        if discentes[1][0] == turmas[0][2]:
            if turmas[1][2] > 0:
                print(f'{discentes[0][0]} matriculado(a) com sucesso na turma {turmas[0][2]}.')
                turmas[1][2] -= 1
            else:
                print(f'Não há vagas na turma {turmas[0][2]}, encaminhando {discentes[0][0]} para a lista de espera...')
                reserva.append(discentes[0][0])
        if discentes[1][0] == turmas[0][3]:
            if turmas[1][3] > 0:
                print(f'{discentes[0][0]} matriculado(a) com sucesso na turma {turmas[0][3]}.')
                turmas[1][3] -= 1
            else:
                print(f'Não há vagas na turma {turmas[0][3]}, encaminhando {discentes[0][0]} para a lista de espera...')
                reserva.append(discentes[0][0])
        del discentes[0][0]
        del discentes[1][0]
        return MatriculaTurmas(turmas, discentes, reserva)

def MatriculaReserva(turmas, reserva):
    if len(reserva) == 0:
        return 0
    else:
        if turmas[1][0] > 0:
            print(f'{reserva[0]} matriculado(a) com sucesso na turma {turmas[0][0]}')
            turmas[1][0] -= 1
        elif turmas[1][1] > 0:
            print(f'{reserva[0]} matriculado(a) com sucesso na turma {turmas[0][1]}')
            turmas[1][1] -= 1
        elif turmas[1][2] > 0:
            print(f'{reserva[0]} matriculado(a) com sucesso na turma {turmas[0][2]}')
            turmas[1][2] -= 1
        elif turmas[1][3] > 0:
            print(f'{reserva[0]} matriculado(a) com sucesso na turma {turmas[0][3]}')
            turmas[1][3] -= 1
        else:
            print(f'Não foi possível matricular {reserva[0]}, não há mais vagas nas turmas.\n')
        del reserva[0]
        return MatriculaReserva(turmas, reserva)


#Programa principal
turmas = [['A1', 'A2', 'B1', 'B2'], [2, 2, 2, 3]]
nome_lista, turma_lista = [], []
print('Bem vindo(a) ao programa de matrículas da escola Burros & Conscientes! Temos as seguintes turmas com vagas:')
ExibicaoTurmas(turmas)
print('Digite o nome do discente e a turma que deseja matricular. Para sair, digite [sair] no campo Nome do discente.')
while True:
    nome_discente = input('Nome discente: ')
    if nome_discente == 'sair':
        break
    nome_lista.append(nome_discente)
    turma_discente = input('Turma discente: ')
    turma_lista.append(turma_discente)
    
discentes = [nome_lista, turma_lista]
reserva = []
reserva = MatriculaTurmas(turmas, discentes, reserva)
if len(reserva) > 0:
    print('\nPrimeira chamada concluída com sucesso, encaminhando a matrícula para lista de espera...\n')
    retorno = MatriculaReserva(turmas, reserva)
    if retorno == 0:
        print('Programa encerrado.')
else:
    print('Todas as matrículas efetuadas com sucesso.\nPrograma encerrado.')