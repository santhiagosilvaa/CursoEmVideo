#leia ano de nascimento e informe
#ainda vai se alistar ; é hora de se alistar ; já passou do tempo de alistamento
#mostrar tempo que falta ou que passou

from datetime import date

nasc = int(input('Qual o seu ano de nascimento? Ex 1996 : '))
ano = date.today().year

idade = ano - nasc

if idade < 18:
    print('Você tem {} ano(s). \nFalta {} ano(s) para se alistar no serviço militar' .format(idade, 18-idade))

elif idade == 18:
    print('Você tem {} anos, está na hora de se alistar. ' .format(idade))

else:
    print('Você tem {} anos. \nJá passou {} ano(s) do tempo de se alistar. ' .format(idade, idade - 18))

