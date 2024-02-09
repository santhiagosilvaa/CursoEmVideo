# leia um numero e mostre seu dobro, tripĺo e raiz quadrada

n1 = int(input('Digite um numero: '))
n2 = n1*2
n3 = n1*3
n4 = n1**(1/2)

print('Seu número é: {}' .format(n1))
print('O dobro é: {}' .format(n2))
print('O triplo é: {}' .format(n3))
print('A raiz quadrada é: {:.2f}' .format(n4))