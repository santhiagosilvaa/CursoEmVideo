#leia o peso, altura, calcule IMC e mostre status
#abaixo de 18.5 - abixo do peso ; entre 18.5 e 25 - peso ideal; 25 até 30 sobrepeso; 30 até 40 obesidade; acima de 40 obesidade mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é de {:.1f}. Você está abaixo do peso. ' .format(imc))

elif 18.5 <= imc <= 25:
    print('Seu IMC é de {:.1f}. Você está no peso ideal. ' .format(imc))

elif 25 < imc <= 30:
    print('Seu IMC é de {:.1f}. Você está com sobrepeso. '.format(imc))

elif 30 < imc <= 40:
    print('Seu IMC é de {:.1f}. Você está com obesidade. ' .format(imc))

else:
    print('Seu IMC é de {:.1f}. Você está com obsidade mórbida. ' .format(imc))