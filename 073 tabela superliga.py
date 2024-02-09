#tupla com nomes do 10 primeiros times
#mostre apenas o 5 primeiros; os ultimos 4; ordem alfabetica; posição do time Praia

superliga = ('Flamengo', 'Minas', 'Osasco', 'Bauru', 'Praia', 'Fluminese', 'Barueri', 'Maringa', 'Pinheiros', 'Brasilia')
pos = superliga.index('Praia')

print(f'Os cinco primeiros times são: {superliga[:5]}')
print(f'Os quartro ultimos times são: {superliga[6:]}')
print(f'Os times em ordem alfabética fica: {sorted(superliga)}')
print(f'O Praia Clube está na posição {pos+1}')