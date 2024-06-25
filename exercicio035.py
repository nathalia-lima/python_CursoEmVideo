# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('primeiro lado: '))
b = float(input('segundo lado: '))
c = float(input('terceiro lado: '))

if (b-c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('é um triângulo')
else:
    print('não é um triângulo')