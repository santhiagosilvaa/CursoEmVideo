#função contador(); inicio fim e passo
#tres contagem -> 1 ate 10 1 em 1; 10 a 0 2 em 2; personalizada

from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.1)
    print()

contador(1, 11, 1)
contador(10, -1, -2)

i = int(input('Digite o valor inicial: '))
f = int(input('Digite o valor final: '))
p = int(input('Digite o passo: '))

if f < i:
    if p > 0:
        p = p*(-1)
        contador(i, f, p)
    elif p < 0:
        contador(i, f, p)

if p == 0:
    if f < i:
        p = -1
        contador(i, f, p)
    else:
        p = 1
        contador(i, f, p)