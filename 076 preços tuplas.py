#crie tuplas com nome e preço
#mostre em forma tabular

produtos = ('Camiseta', 'Calça', 'Tenis', 'Blusa', 'Calular')
preços = ('20.00', '89.90', '350.00', '199.90', '4700.00')

for n in range(0, len(produtos)):
    print(f'{produtos[n]:.<15}R${preços[n]:>8}')
