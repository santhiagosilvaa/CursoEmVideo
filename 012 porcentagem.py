#preço de um produto e valor com desconto de 5%

valor = float(input('Digite o valor do produto: '))
new_valor = valor * (95/100)

print('O valor com 5% de desconto é R${:.2f} (reais)' .format(new_valor))