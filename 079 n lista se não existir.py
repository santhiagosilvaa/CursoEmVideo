#digitar vario valores; lista; se ja exisistir não sera adc e mostrar em ordem crescente

lista = []

while True:
    n = int(input('Digite um numero: '))

    if n not in lista:
        lista.append(n)
    else:
        print('Este numero ja foi inserido.')

    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if op == 'N':
        break

print(f'A lista é: {lista}')
print(f'A lista em ordem crescente é: {sorted(lista)}')