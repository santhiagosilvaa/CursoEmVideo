#leia um numero inteiro; escolha qual será a base de conversão
# 1 binário ; 2 octal; 3 hexadecimal

n = int(input('Digite um número inteiro: '))
base = int(input('Digite o número da opção de conversão desejada: \n1: binário; \n2: octal; \n3: hexadecimal. \nOp: '))

if base == 1:
    print('O número binário de {} é {} ' .format(n, bin(n)[2:]))

elif base == 2:
    print('O númeor octal de {} é {} ' .format(n, oct(n)[2:]))

elif base == 3:
    print('O número hexadecimal de {} é {} ' .format(n, hex(n)[2:]))

else:
    print('Opção inválida.')