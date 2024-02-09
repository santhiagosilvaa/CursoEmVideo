#refaça o ex 35 e mostre o tipo de triangulo
# equilatero ; isosceles; escaleno

a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print('As retas {}, {} e {} formam um triângulo.'.format(a, b, c))

    if (a == b == c):
        print('O triângulo é EQUILÁTERO - todos os lados são iguais.')

    elif (a != b and a != c and b != c):
        print('O triângulo é ESCALENO - todos os lados são diferentes.')

    else:
        print('O triângulo é ISÓSCELES - dois lados são iguais. ')

else:
    print('As retas {}, {} e {} NÃO formam um triângulo.'.format(a, b, c))

