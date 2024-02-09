#função ficha(); nome e gols opcionais, mostrar a ficha msm se incorreto

def ficha(nome='Desconhecido', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s)')

nome = str(input('Digite o nome do jogador: '))
gol = str(input('Quantos gols fez: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(nome='Desconhecido')
else:
    ficha(nome, gol)