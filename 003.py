#Desafio 3 - leia dois numeros e tente mostrar a soma deles
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
soma = numero1 + numero2
print('A soma de',numero1,'+',numero2,'é igual a',soma)
print('A soma de {} + {} é igual a {}.' .format(numero1, numero2, soma))