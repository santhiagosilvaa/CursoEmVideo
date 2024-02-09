#digite 7 numeros -> lista; separe par e impar e mostre em ordem crescente

lista = [[], []]
valor = 0

for c in range(1,8):
    valor = int(input(f'Digite o {c}º numero: '))

    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()
lista[1].sort()
print(f'Os numeros pares em ordem são: {lista[0]}')
print(f'os numeros impares em ordem são: {lista[1]}')