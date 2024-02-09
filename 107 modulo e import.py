#crie modulo operações.py com algumas funçoes e importe
import operações

p = float(input('Digite o preço: R$'))
print(f'A metadade de {p} é {operações.metade(p)}')
print(f'O dobro de {p} é {operações.dobro(p)}')
print(f'Aumentando 10%, temos {operações.aumentar(p, 10)}')
print(f'Diminuir 10%, temos {operações.diminuir(p, 10)}')
