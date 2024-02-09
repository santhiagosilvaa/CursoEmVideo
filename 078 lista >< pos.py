#leia 5 valores, guarde na lista, mostre maior e mnor e suas posições

lista = []


for i in range(1,6):
    n = int(input(f'Digite o {i}º número: '))
    lista.append(n)

print(lista)
print(f'O maior numero da lista é {max(lista)} e está nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}... ', end='')
print(f'\nO menor numero da lista é {min(lista)} está nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}... ', end='')