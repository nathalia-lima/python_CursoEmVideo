# Módulos
# import tudo - está importando tudo do pacote
# from tudo import algo - está importando algo específico do pacote todo

# na documentação pyhton.org tem as bibliotecas nativas
# PyPi - modulos para baixar da comunidade

# Math
# ceil: arredonda pra cima
# floor: // pra baixo
# trunc: coloca só a parte inteira do número
# pow: potência
# sqrt: raiz quadrada
# factorial: fatorial
import math, random

#num = int(input('Digite um número'))
num = random.randint(1, 100)
raiz = math.sqrt(num)
print('A raiz do número {} é: {}' .format(num, raiz))