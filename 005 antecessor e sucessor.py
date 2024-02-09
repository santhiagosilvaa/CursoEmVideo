#leia um numero interio e mostre seu sucessor e antecessor

n1 = int(input('Digite um número inteiro: '))
n2 = n1+1
n3 = n1-1
print('Seu número é: {}' .format(n1))
print('Seu sucessor é {}' .format(n2))
print('Seu antecessor é {}' .format(n3))

print('Seu número é {}, antecessor é {} e sucessor é {}.' .format(n1, n1-1, n1+1))

#menos variaveis economiza memória, mas se for usar o valor a frente é melhor usar variavel
