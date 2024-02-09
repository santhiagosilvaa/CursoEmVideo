#pergunte a distancia de uma viagem
#calcule preço; 0,50 por KM até 200km; 0,45 por km acima de 200

km = float(input('Digite a quilometragem da viagem: '))

if km <= 200:
    preço = 0.5 * km
    print('O preço da passagem para {}km é R${:.2f}' .format(km, preço))

else:
    preço2 = 0.45 * km
    print('O preço da passagem para {}km é R${:.2f}' .format(km, preço2))