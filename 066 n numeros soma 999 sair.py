#leia varios numeros inteiros, só para quando digitar 999, mostre quantos n digitados
# e a soma

n = 0
cont = 0
s = 0

while True:
    n = int(input('Digite um número ou 999 para sair: '))

    if n != 999:
        cont += 1
        s += n

    else:
        print('Fim do programa!')
        break

print(f'Foram digitados {cont} números. ')
print(f'A soma dos números digitas é: {s}')