#jogue par ou impar com PC, interrompe quando jogador perder, mostrando total de vitorias

from random import randint
pc = ''
jog = 0
s = 0
x = 3
vit = 0

while True:
    while x < 1 or x > 2:
        x = int(input('Escolha: \n[1] IMPAR \n[2] PAR \nop: '))

    jog = int(input('Digite a quantidade de numeros desejada para o jogo: '))
    pc = randint(0,11)
    s = jog + pc

    if x == 2:
        if (s % 2) == 0:
            vit += 1
            print(f'Você ganhou. PC = {pc} e Você = {jog}')

        else:
            print(f'Você perdeu após vencer {vit}X. PC = {pc} e Você = {jog}')
            break

    elif x == 1:
        if (s % 2) == 1:
            vit += 1
            print(f'Você ganhou. PC = {pc} e Você = {jog}')

        else:
            print(f'Você perdeu após vencer {vit}X. PC = {pc} e Você = {jog}')
            break
