#crie tupla de 0 a 20 por extenso,
#leia numero e mostre por extenso

n = -1

tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while n not in [0,10]:
    n = int(input('Digite um numero de 0 a 10: '))

print(f'O numero digitado foi {n} = {tupla[n]}')