#leia o nome completo de uma pessoa, mostre o primeiro e ultimo nome separado

nome = input('Digite nome completo: ')
nome1 = nome.split()

print('O nome completo: {}' .format(nome))
print('Nome separado: {}' .format(nome1))

print('O primeiro nome é: {}' .format(nome1[0]))
print('O ultimo nome é: {}' .format(nome1[-1]))