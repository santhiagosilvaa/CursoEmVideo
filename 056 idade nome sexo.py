#lei nome, idade, sexo de 4 pessoas
#média de idade; nome do homem mais velho; quantas mulheres tem menos de 20 anos

idades = []
mediaIdade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for c in range(1,5):
    print('------{}ª PESSOA--------' .format(c))
    nome = str(input('Digite o {}º nome: ' .format(c)))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): '))

    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'F' and idade < 20:
        totmulher20 += 1


    idades.append(idade)


#média de idade
print(idades)
mediaIdade = sum(idades) / len(idades)
print('A média das idades é: {}' .format(mediaIdade))

#nome do homem mais velho
print('O homeM mais velho tem {} anos e se chama {} ' .format(maioridadehomem, nomevelho))

#mulheres menos de 20
print('O total de mulheres abaixo de 20 anos é {} ' .format(totmulher20))