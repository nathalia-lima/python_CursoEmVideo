# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = real / 5.25

print('Com R${} você pode obter US${:.2f}'.format(real, dolar))