# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km percorreu? '))
dias = int(input('Quantos dias de aluguel? '))

valor = (km * 0.15) + (60 * dias)

print('O valor total a pagar será de: R${}'.format(valor) )