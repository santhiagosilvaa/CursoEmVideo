#leia a largara e altura de uma parede em metros, calcule área e quantidade de tinta para pintá-la
# 1l tinta - 2m²

alt = float(input('Digite altura da parede: '))
larg = float(input('Digite a largura da parede: '))

area = alt*larg
tinta = area / 2

print('A área da parede é {}m², e é necessário {}l de tinta para pintá-la.' .format(area, tinta))