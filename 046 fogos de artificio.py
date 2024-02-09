#contagem regressiva p fogos de artificio, 10 até 0, pausa de 1 seg

from time import sleep
import emoji


for fogos in range(10, -1, -1):
    print(fogos)
    sleep(0.5)

print('VIVAAAAA', emoji.emojize(':rocket::collision::sparkler:'))
