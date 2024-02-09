#Digite uma frase -
#quantos A? qual posição a primeira A? qual ultima posição?

frase = str(input('Digite uma frase: ')).upper().strip()

print('Na frase tem {} A' .format(frase.count('A')))
print('O primeiro A está na posição {}' .format(frase.find('A')+1))
print('O ultimo A está na posição {}' .format(frase.rfind('A')+1))
