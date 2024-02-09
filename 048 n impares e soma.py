#calcule a soma entre todos os numeros impares que são multiplos de 3 no intervalo 1 a 500

s = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        s += n

print('A soma dos números ímpares e divisiveis por 3 entre 1 e 500 é: {} ' .format(s))
