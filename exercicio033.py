# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite o primeiro num: '))
num2 = int(input('Digite o segundo num: '))
num3 = int(input('Digite o primeiro num: '))

if num2 < num1 > num3:
    maior = num1
elif num1 < num2 > num3:
    maior = num2
else:
    maior = num3

if num2 > num1 < num3:
    menor = num1
elif num1 > num2 < num3:
    menor = num2
else:
    menor = num3

print('maior {} e menor {}'.format(maior, menor))