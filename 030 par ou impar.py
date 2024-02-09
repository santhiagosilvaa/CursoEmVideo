#leia um numero inteiro e mostre se é par ou impar

n1 = int(input('Digite um número inteiro: '))

if (n1 % 2) == 0:
    print('o número {} é PAR.' .format(n1))

else:
    print('O número {} é IMPAR.' .format(n1))