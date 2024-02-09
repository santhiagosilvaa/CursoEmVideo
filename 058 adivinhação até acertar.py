#melhore o jogo Ex 028, PC vai pensar numero 0 a 10, adivinhar até acertar,
# mostrando quantos palpites para vencer

from random import randint
palpites = 0
n1 = -1
n2 = -2
n1 = randint(0, 10)  # escolher numero aleatoriamente

while n2 != n1:
    n2 = int(input('Adivinhe o numero sorteado de 0 a 10: '))

    palpites += 1

    if n2 != n1:
        print('Número escolhido: {} \nAhh, que pena! Você erro.' .format(n2))

print('=*'*15)
print('Número escolhido: {} \nParabéns, você acertou o número!'.format(n2))
print('Você tentou {}X até acertar. ' .format(palpites))
