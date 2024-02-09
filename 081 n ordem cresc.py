#leia varios numeros e coloque na lista
#quantos foram digitados; em ordem decrescente; valor 5 foi digitado?

lista = []
x = 1

while True:
    n = int(input(f'Digite o {x}º valor: '))
    x += 1
    lista.append(n)

    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if op == 'N':
        break

print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')