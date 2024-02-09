#função area(), largura e comprimento

def area(l, c):
    area = l * c
    print(f'A área do terreno é {area}m²')

l = float(input('Digite a largura do terreno (m): '))
c = float(input('Digite o comprimento (m): '))

area(l, c)