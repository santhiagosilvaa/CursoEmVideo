#leia um numero inteiro e diga se é ou não numero primo

n = int(input('Digite um número: '))
tot = 0

for div in range(1, n+1):
    if n % div == 0:
        tot += 1

if tot <= 2:
    print('O número {} é PRIMO. ' .format(n))

else:
    print('O número {} NÃO é PRIMO. ' .format(n))

print('O numero {} foi divisivel {}x ' .format(n, tot))