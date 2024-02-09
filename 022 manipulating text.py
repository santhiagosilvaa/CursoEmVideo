#leia nome completo
#mostre - nome com todas as letras maiusculas; minusculas; quantas letras ao todo sem espaço; quantas letras o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
separar = nome.split()
sem_espaço = nome.replace(" ", "")

print('Separado: {}' .format(separar))
print('Nome completo: {}.' .format(nome))
print('Nome com letras maiusculas: {}.' .format(nome.upper()))
print('Nome com letras minúsculas: {}.' .format(nome.lower()))
print('Quantas letras ao todo? {}.' .format(len(sem_espaço)))
print('Quantas letras ao todo? {}.' .format(len(nome) - nome.count(" ")))
print('Quantas letras tem o primeiro nome? {} letras' .format(len(separar[0])))
