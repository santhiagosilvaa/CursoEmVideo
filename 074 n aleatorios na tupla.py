#gere 5 numeros aleatorios e colque na tupla
#mostre os numeros e indique o maior e menor

from random import randint

i = 0

tupla = (randint(1, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))

print(f'Os valores sorteados são: {tupla}')
print(f'O maior numero é {max(tupla)}')
print(f'O menor numero é {min(tupla)}')
