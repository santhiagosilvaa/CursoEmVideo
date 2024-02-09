#leia 6 numeros e mostre a soma se forem pares

s = 0
for c in range(1,7):
    n = (int(input('Digite um o {}° número: ' .format(c))))
    if n % 2 == 0:
        s += n

print('A soma dos números pares digitados é {} ' .format(s))