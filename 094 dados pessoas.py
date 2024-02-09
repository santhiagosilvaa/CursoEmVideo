#leia nome, sexo, idade -> dicionario;
#qnts pessoas cadastradas; media idade; lista com mulheres; lista acima da média de idade

dados = {}
op = 0
listadados = []
soma = media = 0

while True:
    dados.clear()
    dados['nome'] = str(input('Digite seu nome: '))
    dados['idade'] = int(input('Digite a idade: '))
    soma += dados['idade']
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO, digite apenas M ou F.')

    listadados.append(dados.copy())

    while True:
        op = str(input('Deseja continuar (S/N)? ')).upper().strip()[0]
        if op in 'SN':
            break
        print('Digite S ou N')
    if op == 'N':
        break

print(f'Ao todo temos {len(listadados)} pessoas cadastradas.')
media = soma/len(listadados)
print(f'A média de idade é {media}')
#mulheres cadastradas
print('AS mulheres cadastradas são: ', end=' ')
for p in listadados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
#média de idade
for p in listadados:
    if p['idade'] > media:
        print(f'{p["nome"]} esta acima da média da idade. Idade {p["idade"]}. Média {media}')


