#leia ano de nascimento e mostre sua categoria
#até 9 anos MIRIM; até 14 INFANTIL; até 19 JUNIOR; até 20 SÊNIOR; acima MASTER

from datetime import date

nasc = int(input('Digite seu ano de nascimento: Ex 1996: '))
idade = date.today().year - nasc

if idade <= 9:
    print('Sua idade é {} e sua categoria é MIRIM. ' .format(idade))

elif idade <= 14:
    print('Sua idade é {} e sua categoria é INFANTIL. ' .format(idade))

elif idade <= 19:
    print('Sua idade é {} e sua categoria é JUNIOR. ' .format(idade))

elif idade <= 20:
    print('Sua idade é {} e sua categoria é SÊNIOR. ' .format(idade))

else:
    print('Sua idade é {} e sua categoria é MASTER. ' .format(idade))
