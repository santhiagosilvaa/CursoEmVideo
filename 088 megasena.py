#ajude na mega sena; pergt quantos jogos; sortear 6 numeros entre 1 e 60, lista composta

from random import randint
from time import sleep

cont = 0
megasena = []
jogo = []

n = int(input('Quantos jogos deseja fazer? '))

for c in range(0,n):
    while True:
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break

    jogo.sort()
    megasena.append(jogo[:])
    jogo.clear()
    cont = 0

for c in range(0,n):
    print(f'{megasena[c]}')
    sleep(0.5)
