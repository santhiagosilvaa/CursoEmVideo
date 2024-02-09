#leia o sexo que só aceita M ou F, caso esteja errado peça novamente

sexo = ""
while sexo not in ['M', 'F']:
    sexo = str(input('Digite o seu sexo (M/F): ')).upper()
    if sexo not in ['M', 'F']:
        print('Digite um sexo válido [M/F].')

print('O sexo do user é {} ' .format(sexo))