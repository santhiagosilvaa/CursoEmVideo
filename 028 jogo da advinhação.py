#PC "pensa" em um numero, usuario adivinha, escrever se venceu ou não

from random import randint

n1 = randint(0,5) #escolher numero aleatoriamente

n2 = int(input('Adivinhe o numero sorteado de 0 a 5: '))

if n2 == n1:
    print('Número escolhido: {} \nParabéns, você acertou o número!' .format(n2))

else:
    print('Número escolhido: {} \nAhh, que pena! Você erro. Número sorteado foi: {}' .format(n2, n1))