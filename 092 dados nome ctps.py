#leia nome, ano de nasc e carteira trabalho, cadastre com idade
#se CTPS for dif de 0 -> ano contratação e salario; calcule quantos anos vai aposentar

from datetime import date

dados = {}

dados['Nome'] = str(input('Digite o nome: '))

nasc = int(input('Digite ano de nascimento: '))
dados['idade'] = date.today().year - nasc

dados['ctps'] = int(input('Nº CTPS ou 0 se não tiver: '))

if dados['ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    #35 anos de contribuição
    dados['aposentar'] = dados['Contratação'] + 35 - nasc


for k, v in dados.items():
    print(f'{k} tem valor {v}')

