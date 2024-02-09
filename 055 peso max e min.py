#leia peso de cinco pessoas, mostre maior e o menor

pesos = [] #lista

for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: ' .format(c)))
    pesos.append(peso) #adiciona os pesos na lista

print('Lista: {}' .format(pesos))
print('O peso máximo é: {} ' .format(max(pesos)))
print('O peso mínimo é {} ' .format(min(pesos)))