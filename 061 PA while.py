#refaça 051 usando while

a = int(input('Digite o primeiro termo da PA: '))
d = int(input('Digite a razão da PA: '))
n = int(input('Digite o número de termos: '))

termos = []

while n in range(1, n+1):
#for n in range(1, n+1):
    s = a + (n-1)*d
    n -= 1
    termos.append(s)

print('Os termos da PA são: {}' .format(termos[::-1]))