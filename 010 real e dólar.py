#digite valor em dinheiro e converta para dolar

real = float(input('Digite quanto de dinheiro você tem em reais: '))
dol = real / 3.27

print('Você tem R${} (Reais) e ${:.2f} (Dólar)' .format(real, dol))