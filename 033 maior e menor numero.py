#leia tres numeros e mostre qual maior e qual menor

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo númeor: '))
n3 = float(input('Digite o terceiro número: '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print('O maior número é {}' .format(maior))
print('O menor número é {}' .format(menor))