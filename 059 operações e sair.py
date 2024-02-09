#leia dois valores e mostre
#[1] SOMAR [2] MULTIPLICAR [3] MAIOR [4] NOVOS NÚMEROS [5] SAIR DO PROGRAMA


result = 0
op = 0

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while op != 5:

    op = int(input('Escolha a opção desejada: \n[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA \nOp: '))

    if op == 1:
        result = n1 + n2
        print('O resultado da soma é {} '.format(result))

    elif op == 2:
        result = n1 * n2
        print('O resultado da multiplicação é {} '.format(result))

    elif op == 3:
        result = max(n1, n2)
        print('O valor máximo é {} '.format(result))

    elif op == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

    elif op == 5:
        print('Você saiu do programa. Até mais')

    else:
        print('Digite uma opção válida.')

print('FIM')