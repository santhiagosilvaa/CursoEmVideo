#aprimore o 093; varias pessoas e detalhe de cada jogador

dados = {}
listadados = []
gols = []
cont = 0
i = 0

while True:
    dados.clear()
    gols.clear()
    dados['nome'] = str(input('Digite o nome do jogador: '))

    partidas = int(input('Quantas partidas jogou? '))
    for p in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {p+1}: '))
        p += 1
        gols.append(gol)

    dados['Gols'] = gols[:]
    dados['total'] = sum(gols)

    listadados.append(dados.copy())
    cont += 1

    while True:
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if op in 'SN':
            break
        print('Digite S ou N')
    if op == 'N':
        break

print('-=' * 30)
print(F'{"COD":<3} {"NOME":<10} {"GOLS":<10} {"TOTAL":<3}')
for j in listadados:
    print(f'{i+1:<3} {j["nome"]:<10} {j["Gols"]} {j["total"]:>3}')
    i += 1
print('-=' * 30)

while True:
    n = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if n == 999:
        break
    if n > len(listadados):
        print('Erro. Digite opção correta.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {listadados[n-1]["nome"]}')
        for i, g in enumerate(listadados[n-1]['Gols']):
            print(f'Na partida {i+1}, fez {g} gols')