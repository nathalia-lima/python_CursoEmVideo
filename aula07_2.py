n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
mod = n1 % n2

print('A soma é {}, a diferença é {}, o produto é {} e a divisão é {:.3f}'.format(s, sub, m, d), end='; ')
print('Divisão inteira {}, Exponenciação {} e Módulo {}'.format(di, e, mod))

