#mostre tabuada de varios numeros, para quando digitar numero negativo
n = 0

while True:
    print('_' * 20)
    n = int(input('Digite um numero para fazer a tabuada ou um numero negativo para sair: '))

    if n > 0:
        print('=*'*10)
        print(f'A tabuada do {n} é: ')
        print('=*' * 10)
        for i in range(1, 11):
            result = n * i
            print(f'{n:2} X {i:2} = {result:2}')

    else:
        print('Você digitou um número negativo. Fim do programa. ')
        break
