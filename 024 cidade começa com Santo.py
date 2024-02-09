#leia nome de uma cidade e diga se começa ou não com "Santo"

cidade = str(input('Digite o nome da cidade: ')).strip()
nome1 = cidade.capitalize().split()
n = 'Santo' in nome1[0]

print('Cidade: {}' .format(cidade))
print('Começa com Santo? {}' .format(n))