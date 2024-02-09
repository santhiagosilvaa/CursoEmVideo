#digite 5 valores e cadastre na lista na posição do menor para maior

lista = []

for i in range(0,5):
    n = int(input('Digite um valor: '))

    if i == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print(f'Adicionado ao final da lista')

    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1

print(lista)

