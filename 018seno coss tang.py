#leia angulo e calcule seno, cosseno e tangente
import math

ang = float(input('Digite o angulo: '))
angR = math.radians(ang) #radiano

seno = math.sin(angR) #seno
coss = math.cos(angR) #cosseno
tang = math.tan(angR) #tangente

print('Com o angulo de {}º, temos: \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}' .format(ang, seno, coss, tang))