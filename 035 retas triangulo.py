# leia 3 retas e diz se podem formar um triangulo

a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print('As retas {}, {} e {} formam um triângulo.'.format(a, b, c))

else:
    print('As retas {}, {} e {} NÃO formam um triângulo.'.format(a, b, c))
