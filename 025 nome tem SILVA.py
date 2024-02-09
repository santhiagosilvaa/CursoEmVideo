#Leia o nome de uma pessoa e diga se tem SILVA

nome = str(input('Digite seu nome completo: ')).strip()

print('No nome tem SILVA? {}' .format('SILVA' in nome.upper()))