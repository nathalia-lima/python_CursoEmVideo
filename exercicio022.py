# Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('Nome em letras maiusculas: {}, e em minusculas: {}'.format(nome.upper(), nome.lower()))
print('Quantas letras possui: {}'.format(len(nome) - nome.count(' ')) )

primeiro = nome.split()
print('Primeiro nome qtde de letras: {}'.format(len(primeiro[0])))

print('Primeiro nome qtde de letras: {}'.format(nome.find(' ')))


