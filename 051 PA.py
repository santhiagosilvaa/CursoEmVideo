#leia o primeiro termo e a razão de uma PA e mostre os 10 primeiros termos dessa progressçao

a = int(input('Digite o primeiro termo da PA: '))
d = int(input('Digite a razão da PA: '))
n = int(input('Digite o número de termos: '))

termos = []

for n in range(1, n+1):
    s = a + (n-1)*d
    termos.append(s)

print('Os termos da PA são: {}' .format(termos))

