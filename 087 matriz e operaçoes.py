#aprimore o ex anterior e mostre a soma de todos os pares; soma da 3 coluna; maior da 2 linha

soma = somaC = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
listaM = []

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para posição {l}x{c}: '))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

print(f'A soma dos valores pares é: {soma}')

for l in range(0,3):
    for c in range(2,3):
        somaC += matriz[l][c]

print(f'A soma da terceira coluna é: {somaC}')

for l in range(1,2):
    for c in range(0,3):
        listaM.append(matriz[l][c])
print(f'O maior valor da 2ª linha é: {max(listaM)}')
