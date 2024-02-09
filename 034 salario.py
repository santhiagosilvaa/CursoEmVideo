#pergunte salario; calcule aumento
#> 1250 - 10% ; <= 15%

sal = float(input('Digite seu salário: R$'))

if sal > 1250:
    sal1 = sal * 1.1
    print('Seu novo salário será R${:.2f}' .format(sal1))

else:
    sal2 = sal * 1.15
    print('Seu novo salário será R${:.2f}' .format(sal2))