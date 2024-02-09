#leia numero Real e mostre sua porção inteira

import math
n = float(input('Digite um numero real (x.xx):' ))
n1 = math.floor(n) #arredonda numero para baixo

print('Número digitado: {}. \nNúmero inteiro: {}' .format(n, math.floor(n)))
print('Número digitado: {}. \nNúmero inteiro: {}' .format(n, n1))

print('Número digitado: {}. \nNúmero inteiro: {}' .format(n, int(n)))
print('Número digitado: {}. \nNúmero inteiro: {:.0f}' .format(n, n))
