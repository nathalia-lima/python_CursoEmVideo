#  Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

escolha = int(input('Digite um número entre 0 e 5: '))

num = random.randint(0, 5)

if escolha == num:
    print('Acertou: {}'.format(num))
else:
    print('Errou: {}'.format(num))