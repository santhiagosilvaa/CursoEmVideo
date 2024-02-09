#modifique o 108

import operações

p = float(input('Digite o preço: R$'))
print(f'A metadade de {operações.moeda(p)} é {operações.metade(p, True)}')
print(f'O dobro de {operações.moeda(p)} é {operações.dobro(p, True)}')
print(f'Aumentando 10%, temos {operações.aumentar(p, 10, True)}')
print(f'Diminuir 10%, temos {operações.diminuir(p, 10, True)}')