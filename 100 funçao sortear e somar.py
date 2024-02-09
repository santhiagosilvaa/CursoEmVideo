#lista - numeros; duas funçoes sorteia() e somaPar(), sortear 5 numeros e somar os pares
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores entre 1 e 10: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('Pronto')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somanda os pares de {lista} temos {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)