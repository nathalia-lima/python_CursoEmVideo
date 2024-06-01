# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um número: '))
d = n1 * 2
t = n1 * 3
r = n1**2

print('O dobro de {} vale {}\nO triplo de {} vale {}\nA raiz quadrada de {} vale {:2f}'.format(n1, d, n1, t, n1, r))