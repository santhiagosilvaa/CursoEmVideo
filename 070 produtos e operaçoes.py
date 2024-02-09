#leia nome e preço de varios produtos, pergt se quer continuar
# total gasto; quantos custam mais de 1000; nome do mais barato

cont = 1
total = 0
val1000 = 0
listaP = []
listaN = []
pos = 0
x = 0
barato = 0

while x != 'N':
    nome = str(input(f'Qual o nome do {cont}º produto? '))
    cont += 1
    preço = float(input('Qual o valor desse produto? R$'))

    total += preço

    listaP.append(preço)
    listaN.append(nome)

    if preço > 1000:
        val1000 += 1

    x = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    pos = listaP.index(min(listaP))
    barato = listaN[pos]

    if x == 'S':
        continue
    elif x == 'N':
        break
    else:
        print('Valor inválido.')
        x = str(input('Deseja continuar? [S/N]: ')).upper()

print(f'O total gasto na compra é de R${total}')
print(f'{val1000} produtos custam mais de R$1000')
print(f'O produto mais barato é {barato} e custa R${listaP[pos]}')