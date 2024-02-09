#leia um numero de 0 a 9999 e mostre separados: unidade, dezena, centena, milhar

n1 = int(input('Digite um numero de 0 a 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print('Unidade: {}' .format(u))
print('Dezena: {}' .format(d))
print('Centena: {}' .format(c))
print('milhar: {}' .format(m))