#pergunte quantidade de KM percorrido e qntd de dias alugado - calcule o preço a pagar
#R$60 por dia, R$0.15 por KM

km = float(input('Quantos KM foi percorrido? '))
dia = float(input('Quantos dias foi alugado: '))

valor_dia = 60 * dia
valor_km = 0.15 * km
soma = valor_dia + valor_km

print('Ao percorrer {}km e alugar por {} dias, você pagará no total R${}. \nR${} pela quilometragem e R${} pelos dias' .format(km, dia, soma, valor_km, valor_dia))
