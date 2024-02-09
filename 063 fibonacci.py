#leia numero inteiro e mostre os n primeiros elementos de uma sequencia de fibonacci

n = int(input('Quantos elementos deseja: '))

a1 = 0
a2 = 1
ele = 3

print('{} -> {}' .format(a1, a2), end='')

while ele < n+1:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    ele += 1
    print(' -> {}' .format(a3), end='')



