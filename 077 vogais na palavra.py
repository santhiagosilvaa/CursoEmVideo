#tupla com varias palavras, mostrar as vogais

superliga = ('Flamengo', 'Minas', 'Osasco', 'Bauru', 'Praia', 'Fluminese', 'Barueri', 'Maringa', 'Pinheiros', 'Brasilia')
vogais = 'aerioAEIOU'

for n in superliga:
    print(f'\nO time é {n}: ', end=" ")

    for letra in n:
        if letra in 'aeiouAEIOU':
            print(letra, end=" ")