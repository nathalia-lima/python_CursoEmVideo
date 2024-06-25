# Manipulando texto

# Fatiamento

frase = 'Olá, tudo bem!'

print(frase[8])
print(frase[8:13])
print(frase[8:13:2])
print(frase[:13])
print(frase[2::3])

print(len(frase))
print(frase.count('o'))
print(frase.count('o', 3, 13))
print(frase.find('tudo'))
print('Olá' in frase)

# Transformação 

print(frase.replace('Olá', 'Bom dia'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
# remove espaços extras print(frase.strip()), espaço da direita print(frase.rstip()) assim como l da esquerda
print(frase.strip())
# Divisão
 
print(frase.split())

#Junção

print('-'.join(frase))