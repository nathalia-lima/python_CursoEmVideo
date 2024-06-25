# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Nome completo: '))

primeiro = nome.split()
print('Primeiro nome: {}'.format(primeiro[0]))
print('PrimeiUltimoro nome: {}'.format(primeiro[-1]))