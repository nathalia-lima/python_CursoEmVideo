# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as possíveis informações sobre ele

n = input('Digite algo: ')
print(type(n))
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaços?', n.isspace())
print('E um numero?', n.isnumeric())
print('E alfabetico?', n.isalpha())
print('E alfanumerico?', n.isalnum())
print('Esta em maiusculas?', n.isupper())