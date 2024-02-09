#leia varios numeros inteiros, mostre a média, maior e menor, e se quer continuar ou não

n = 1
op = ""
lista = []
cont = 0

while op in 'S':
    n1 = int(input('Digite o {}º número: ' .format(n)))
    n += 1
    cont += 1
    lista.append(n1)

    op = str(input('Deseja digitar mais números? [S/N]: ')).upper()

s = sum(lista)
print(lista)
print('A média dos valores digitados é: {} ' .format(s/cont))
print('O maior valor é: {} ' .format(max(lista)))
print('O menor valor é: {} ' .format(min(lista)))