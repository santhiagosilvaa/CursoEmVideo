#leia nome e peso, guarde lista;
#quantas pessoas; mais pesados; mais leves

lnome = []
lpeso = []

while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    lnome.append(nome)
    lpeso.append(peso)

    op = str(input('Deseja cadastrar mais nomes? [S/N]: ')).upper().strip()[0]

    if op == 'N':
        break

print(f'Foram cadastradas {len(lnome)} pessoas.')

print(f'\nAs pessoas mais pesadas são:', end=' ')
for i, v in enumerate(lpeso):
    if v == max(lpeso):
        print(f'{lnome[i]}...', end=' ')

print(f'\nAs pessoas mais leves são: ', end= ' ')
for i, v in enumerate(lpeso):
    if v == min(lpeso):
        print(f'{lnome[i]}...', end=' ')

