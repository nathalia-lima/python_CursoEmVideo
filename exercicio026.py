# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).lower()

print(frase.count('a'))

print(frase.find('a')+1)
print(frase.rfind('a')+1)