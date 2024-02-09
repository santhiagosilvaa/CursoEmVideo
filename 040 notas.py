#leia duas notas e calcule a média
# abaixo de 5 reprovado ; entre 5 e 6.9 recuperação; 7 ou maior aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m < 5.0:
    print('Sua nota é {:.1f}. \nVocê está \033[41mREPROVADO\033[m' .format(m))

elif 5 <= m <= 6.9:
    print('Sua nota é {:.1f}. \nVocé está em \033[43mRECUPERAÇÃO\033[m' .format(m))

else:
    print('Sua nota é {:.1f}. \nVocê está \033[42mAPROVADO\033[m' .format(m))