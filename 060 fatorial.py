#leia numero e mostre seu fatorial

n1 = int(input('Digite um numero inteiro: '))
fat = 1
n2 = n1

while n1 > 1:
    fat *= n1
    n1 -= 1
print('O resultado do fatorial de {} é {}' .format(n2, fat))