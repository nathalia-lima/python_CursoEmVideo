# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Distancia da viagem em Km: '))

'''if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
'''

valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('Valor da passagem: {}'.format(valor))