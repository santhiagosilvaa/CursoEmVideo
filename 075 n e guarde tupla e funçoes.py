#leia 4 valores e guarde na tupla
#quantos 9; posição do 3; quais são pares


tupla = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite outro numero: ')))

print(tupla)
print(f'Tem {tupla.count(9)} nove(s).')

if 3 in tupla:
    print(f'O 3 está na posição {tupla.index(3)+1}')
else:
    print('Não tem o numero 3')

print('Os valores pares digitados foram: ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

