#leia varios numeros -> lista;
#crie duas listas extras -> pares e impares; mostre os 3

lista = []
listaP = []
listaI = []

while True:
    n = int(input('Digite um numero: '))
    lista.append(n)

    if n % 2 == 0:
        listaP.append(n)
    else:
        listaI.append(n)

    op = str(input('Deseja digitar mais numeros? [S/N]: ')).upper().strip()[0]
    if op == 'N':
        break

print(f'Lista completa: {lista}')
print(f'Pares: {listaP}')
print(f'Impares: {listaI}')
