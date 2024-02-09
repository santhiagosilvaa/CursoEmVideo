#leia comprimento do cateto oposto e adjacente, calcule a hipotenusa
import math
from math import hypot #economiza espaço - não precisa chamar import na função abaixo

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

hp = math.sqrt(co**2 + ca**2) #sqrt raiz quadrada
hp1 = hypot(co, ca) #hipotenusa

print('O comprimento da hipotenusa é {:.2f}cm.' .format(hp))
print('O comprimento da hipotenusa é {:.2f}cm.' .format(hp1))