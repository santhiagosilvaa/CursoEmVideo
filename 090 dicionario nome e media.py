#nome e média e diz se aprovado ou reprovado

lista = {}

lista['nome'] = str(input('Nome: '))
lista['media'] = float(input('Média: '))

if lista['media'] < 7:
    lista['Situação'] = 'REPROVADO'
else:
    lista['Situação'] = 'APROVADO'

for k, v in lista.items():
    print(f'{k} é igual a {v}')