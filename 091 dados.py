#4 jogadores; result aleatorio 1 a 6 , guarde em um dicionario; coloque em ordem

lista = {}

from random import randint
from operator import itemgetter

lista = {'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)}

ordem = {}

print('Valores sorteado')
for k, v in lista.items():
    print(f'{k} tirou {v} no dado')

print('O ganhador foi')
ordem = sorted(lista.items(), key=itemgetter(1), reverse=True)
for k, v in ordem:
    print(f'{k} tirou {v} no dado')
