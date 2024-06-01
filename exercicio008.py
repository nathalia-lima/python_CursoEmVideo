# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite um valor em metros: '))
cm = n * 100
mm = n * 1000

print('O valor {} em centímetros e {} em milímetros'.format(cm, mm))