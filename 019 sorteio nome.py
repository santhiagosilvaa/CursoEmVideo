#sortear 1 aluno entre 4 e mostrar nome

import math
import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

nomes = [n1, n2, n3, n4]

sortear = random.choice(nomes) #sorteio de nomes
print('O aluno escolhido é: {}' .format(sortear))