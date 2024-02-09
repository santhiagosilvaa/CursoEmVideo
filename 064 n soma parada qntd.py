#leia varios numeros inteiros, só pare quando digitar 999, mostre qnts numeros digitados e a soma

lista = []
n1 = 0
cont = 0

while n1 != 999:
    n1 = int(input('Digite um numero inteiro ou 999 para finalizar: '))

    if n1 == 999:
        break

    else:
        lista.append(n1)
        cont += 1
        continue

print(lista)
print('A quantidade de numeros digitados foi: {} ' .format(cont))
print('A soma dos números digitados é: {} ' .format(sum(lista)))