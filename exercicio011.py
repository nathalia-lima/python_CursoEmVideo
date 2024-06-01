# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))

area = l * a
tinta = area / 2

print('Para pintar essa parede que possui area de {}, precisaremos de {} litros de tinta'.format(area, tinta))