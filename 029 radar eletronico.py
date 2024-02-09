# leia a velocidade de um carro;
# se > 80km/h - msg dizendo que foi multado - R$7 cada KM acima do limite

v1 = float(input('Digite a velocidade que estava: '))
v2 = float(input('Qual a velocidade máxima permitida? '))

if v1 > v2:
    multa = (v1 - v2) * 7
    print('Você ultrapassou a velocidade máxima da via. \nMulta de R${}.' .format(multa))

else:
    print('Você não ultrapassou a velocidade máxima.')