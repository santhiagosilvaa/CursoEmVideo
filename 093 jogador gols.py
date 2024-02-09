#ler nome jogador; quantas partidas; gols em cada partida; total de gols

dados = {}
gols = []

dados['nome'] = str(input('Digite o nome do jogador: '))

partidas = int(input('Quantas partidas jogou? '))
for p in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {p+1}: '))
    p += 1
    gols.append(gol)

dados['Gols'] = gols[:]
dados['total'] = sum(gols)

print('-=' * 30)
print(dados)

print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')

print('-=' * 30)
print(f'O jogado {dados["nome"]} jogou {partidas} partidas.')
for p in range(0, partidas):
    print(f'Na partida {p+1}, fez {gols[p]} gols')
print(f'Fez o total de {dados["total"]} gols')