# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input("Digite o ângulo:"))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('Ângulo: {}\nO seno é: {:.2f}\nO cosseno é: {:.2f}\nA tangente é: {:.2f}' .format(angulo, sen, cos, tan))
