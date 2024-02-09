#leia ano de nasc de sete pessoas, mostre quantas não atingiram maioridade e quantas já são maiores

from datetime import date

n = 0
x = 0

for c in range(1, 8):
    ano = int(input('Digite o {}° ano de nascimento: ' .format(c)))

    if date.today().year - ano < 21:
        n = 1 + n

    else:
        x = 1 + x

print('{} pessoas não atingiram a maioridade. ' .format(n))
print('{} pessoas atingiram a maioridade '.format(x))
