# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tipo = str(input('Digite a letra conforme o tipo de temperatura escolhida:\nC - Celsius\nF - Fahrenheit\n'))
temperatura = float(input('Digite a temperatura: '))


if (tipo == 'C' or tipo == 'c'):
    print('A temperatura {}°C em fahrenheit fica {}°F'.format(temperatura, (temperatura * 1.8 + 32) ))
elif (tipo == 'F' or tipo == 'f'):
    print('A temperatura {}°F em celsius fica {}°C'.format(temperatura, ((temperatura - 32) / 1.8) ))
else:
    print('Valor inválido!')
