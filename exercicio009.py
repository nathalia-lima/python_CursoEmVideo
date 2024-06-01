# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n1 = int(input('Digite um número: '))

print('-' * 12)
for c in range(1, 11):
    print('{} x {} = {}'.format(n1, c, n1 * c))
print('-' * 12)