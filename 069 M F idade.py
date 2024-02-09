#leia idade e sexo de varias pessoas, pergtando se quer continuar
# quantas tem mais de 18; quantos homens; quantas mulheres menos de 20 anos

x = ''
cont = 1
id = 0
h = 0
idf = 0
sexo = ' '

while x != 'N':
    while sexo not in 'MF':
        sexo = str(input(f'Digite o sexo da pessoa [M/F]: ')).upper().strip()[0]
    idade = int(input('Digite a idade: '))
    cont += 1

    x = str(input('Deseja digitar mais nomes? [S/N]: ')).upper().strip()[0]

    if idade > 18:
      id += 1

    if sexo == 'M':
        h += 1

    else:
        if idade < 20:
            idf += 1

print(f'Temos {id} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {h} homens.')
print(f'Temos {idf} mulheres abaixo de 20 anos.')


