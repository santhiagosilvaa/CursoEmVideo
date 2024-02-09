#leia uma frase e diga se é um políndromo

frase = str(input('Digite uma frase: '))
frase1 = frase.replace(" ", "")
frase2 = frase1[::-1]
print(frase1)
print(frase2)

if frase1 == frase2:
    print('A frase: {} é um políndromo: {}' .format(frase, frase2))

else:
    print('Não é um políndromo')