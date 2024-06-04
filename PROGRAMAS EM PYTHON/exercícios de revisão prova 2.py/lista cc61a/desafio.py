'''
Escreva um programa em Python que utilize recursividade para calcular o consumo total de
combustível de um carro em uma viagem. O programa deve:
• Permitir que o usuário insira os seguintes dados:
• Distância total da viagem (em quilômetros).
• Consumo médio do carro (em litros por quilômetro).
• Distância inicial do percurso (opcional, para calcular o consumo em etapas).
• Exibir o consumo total de combustível da viagem.
• Validar a entrada do usuário, garantindo que os valores sejam positivos.
'''
#Funções
def CalculoConsumo (Distancia_Total, ConsumoMedio):
        Consumo = Distancia_Total / ConsumoMedio
        return Consumo

def CalculoTrechos(m):
        if len(m) == 0:
            return 0
        else: 
            trecho = m[0]
            comb = trecho[0] / trecho[1]
            print(f'O consumo no trecho {m[0]} é: {comb} litros.')
            del (m[0])
            return comb + CalculoTrechos(m)

def Menu():
      print('Bem vindo, selecione a opção que deseja:\n[1] Calcular consumo a partir da distância total\n[2] Calcular a partir de trechos')
      r = int(input(''))
      return r

def AtribuicaoMatriz(m):
      lista = [0] * 2
      r = 0
      while True:
            if r == 0:
                  lista[0] = float(input('Digite a distância do trecho (em km): '))
                  lista[1] = float(input('Digite o consumo médio do carro no trecho (em litros por km): '))
                  m.append(lista)
                  print('[0] Continuar\n[1] Sair ')
                  r = int(input(' '))
            if r == 1:
                  break

def CalculoPreco(ConsumoTotal):
      Preco = (ConsumoTotal * 5.85)
      return Preco

#Programa principal
r = Menu()
if r == 1:
    print('Vamos calcular o consumo total de combustível: ')
    DistanciaTotal = float(input('Digite a distância total da viagem (em km): '))
    ConsumoMedio = float(input('Digite o consumo médio do carro (em litros por km): '))
    ConsumoTotal = round(CalculoConsumo(DistanciaTotal, ConsumoMedio), 2)
    print(f'O consumo total do carro é: {ConsumoTotal} litros.')
    Preco = round(CalculoPreco(ConsumoTotal), 2)
    print(f'O preço total da viagem é: R${Preco}.')
if r == 2:
    m = []
    AtribuicaoMatriz(m)
    ConsumoTotal = round(CalculoTrechos(m), 2)
    print(f'O consumo total é de: {ConsumoTotal} litros.')
    Preco = round(CalculoPreco(ConsumoTotal), 2)
    print(f'O preço total da viagem é: R${Preco}.')
