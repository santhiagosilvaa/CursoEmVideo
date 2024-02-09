#leia dois numeros inteiros e compare-os
#o primeiro valor é maior
#o segundo valor é maior
#os dois são iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('O primeiro valor é maior. \n{} > {}' .format(n1, n2))

elif n1 < n2:
    print('O segundo valor é maior. \n{} > {}' .format(n2, n1))

else:
    print('Não existe valor maior, os dois são iguais. \n{} = {} ' .format(n1, n2))

