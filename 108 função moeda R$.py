#modifique o 107 para colocar o simbolo de moeda

import operações

p = float(input('Digite o preço: R$'))
print(f'A metadade de {operações.moeda(p)} é {operações.moeda(operações.metade(p))}')
print(f'O dobro de {operações.moeda(p)} é {operações.moeda(operações.dobro(p))}')
print(f'Aumentando 10%, temos {operações.moeda(operações.aumentar(p, 10))}')
print(f'Diminuir 10%, temos {operações.moeda(operações.diminuir(p, 10))}')